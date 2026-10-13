"""CLI entry point for the CASE/UCO code generator."""

from __future__ import annotations

import argparse
import dataclasses
import json
import logging
import re
import sys
from pathlib import Path

from case_uco_generator.ontology_parser import (
    parse_ontology,
    load_extension_manifest,
)
from case_uco_generator.backends.python_backend import PythonBackend
from case_uco_generator.backends.csharp_backend import CSharpBackend
from case_uco_generator.backends.java_backend import JavaBackend
from case_uco_generator.backends.rust_backend import RustBackend
from case_uco_generator.backends.docs_backend import DocsBackend
from case_uco_generator.mapping_guide import generate_mapping_guide
from case_uco_generator.scaffold import scaffold_extension


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="case-uco-generate",
        description="Generate CASE/UCO ontology libraries from OWL+SHACL Turtle files.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # --- generate subcommand ---
    gen_parser = subparsers.add_parser("generate", help="Generate typed libraries from ontology sources")
    gen_parser.add_argument(
        "--lang",
        choices=["python", "csharp", "java", "rust", "all"],
        default="all",
        help="Target language (default: all)",
    )
    gen_parser.add_argument("--ontology-dir", type=Path, default=None)
    gen_parser.add_argument("--output-dir", type=Path, default=None)
    gen_parser.add_argument("--extensions-dir", type=Path, default=None)
    gen_parser.add_argument("--no-extensions", action="store_true")

    # --- scaffold subcommand ---
    scaf_parser = subparsers.add_parser(
        "scaffold",
        help="Generate starter classes from an extension ontology TTL",
    )
    scaf_parser.add_argument(
        "--extension",
        type=Path,
        required=True,
        nargs="+",
        help="Path(s) to extension .ttl file(s) (OWL + SHACL shapes)",
    )
    scaf_parser.add_argument(
        "--lang",
        choices=["python", "csharp", "java", "rust", "all"],
        default="all",
        help="Target language(s) for scaffolded classes (default: all)",
    )
    scaf_parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for scaffolded files (default: current directory)",
    )

    # --- generate-extension subcommand ---
    ext_parser = subparsers.add_parser(
        "generate-extension",
        help="Generate complete publishable packages from an extension manifest",
    )
    ext_parser.add_argument(
        "--extension",
        type=Path,
        required=True,
        help="Path to the extension directory containing manifest.json",
    )
    ext_parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for generated packages (default: packages/case-uco-<name>)",
    )
    ext_parser.add_argument(
        "--lang",
        choices=["python", "csharp", "java", "rust", "all"],
        default="all",
        help="Target language(s) (default: all)",
    )
    ext_parser.add_argument("--ontology-dir", type=Path, default=None)

    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "generate":
        return _cmd_generate(args)
    elif args.command == "scaffold":
        return _cmd_scaffold(args)
    elif args.command == "generate-extension":
        return _cmd_generate_extension(args)

    return 0


def _cmd_generate(args) -> int:
    repo_root = args.output_dir or Path.cwd()
    ontology_dir = args.ontology_dir or repo_root / "ontology"
    if args.no_extensions:
        extensions_dir = None
    elif args.extensions_dir:
        extensions_dir = [args.extensions_dir]
    else:
        # v1.19.0: SDK-native extensions plus upstream-vendored ontologies.
        extensions_dir = [repo_root / "extensions", repo_root / "ontology"]

    if not ontology_dir.exists():
        logging.error("Ontology directory not found: %s", ontology_dir)
        return 1

    logging.info("Parsing ontology from %s ...", ontology_dir)
    schema = parse_ontology(ontology_dir, extensions_dir=extensions_dir)
    logging.info(
        "Parsed %d classes, %d vocabs across %d modules",
        len(schema.classes), len(schema.vocabs), len(schema.modules),
    )

    languages = (
        ["python", "csharp", "java", "rust"]
        if args.lang == "all"
        else [args.lang]
    )

    core_schema = schema.without_extensions()
    output_root = repo_root
    total_files = 0
    for lang in languages:
        logging.info("Generating %s library ...", lang)
        backend = _create_backend(lang, core_schema, output_root)
        files = backend.generate()
        total_files += len(files)
        logging.info("  -> %d files generated for %s", len(files), lang)

    logging.info("Generating ontology reference ...")
    docs_backend = DocsBackend(schema, output_root)
    docs_files = docs_backend.generate()
    total_files += len(docs_files)
    logging.info("  -> %s", docs_files[0])

    logging.info("Generating mapping guide ...")
    guide_path = generate_mapping_guide(schema, output_root / "docs" / "MAPPING_GUIDE.md")
    total_files += 1
    logging.info("  -> %s", guide_path)

    logging.info("Generating runtime registry (full schema with extensions) ...")
    registry_backend = PythonBackend(schema, output_root / "python" / "case_uco")
    registry_path = registry_backend._emit_registry()
    logging.info("  -> %s", registry_path)

    registry_copies = {
        "csharp": output_root / "csharp" / "CaseUco" / "_registry.json",
        "java": output_root / "java" / "src" / "main" / "resources" / "_registry.json",
        "rust": output_root / "rust" / "src" / "_registry.json",
    }
    import shutil
    for lang_name, dest in registry_copies.items():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(registry_path, dest)
        total_files += 1
        logging.info("  -> %s (%s)", dest, lang_name)

    logging.info("Done: %d total files generated.", total_files)
    return 0


def _cmd_scaffold(args) -> int:
    ttl_paths = [Path(p) for p in args.extension]
    for p in ttl_paths:
        if not p.exists():
            logging.error("Extension file not found: %s", p)
            return 1

    languages = (
        ["python", "csharp", "java", "rust"]
        if args.lang == "all"
        else [args.lang]
    )

    output_dir = args.output_dir or Path.cwd()
    logging.info("Scaffolding extension from %s ...", ", ".join(str(p) for p in ttl_paths))

    created = scaffold_extension(ttl_paths, output_dir, languages)

    if not created:
        logging.warning("No classes found. Ensure the TTL has OWL classes with SHACL NodeShapes.")
        return 1

    logging.info("Done: %d scaffolded files created.", len(created))
    return 0


def _create_backend(lang: str, schema, output_root: Path):
    backends = {
        "python": (PythonBackend, output_root / "python" / "case_uco"),
        "csharp": (CSharpBackend, output_root / "csharp" / "CaseUco"),
        "java": (JavaBackend, output_root / "java" / "src" / "main" / "java" / "org" / "caseontology"),
        "rust": (RustBackend, output_root / "rust" / "src"),
    }
    cls, out_dir = backends[lang]
    return cls(schema, out_dir)


def _cmd_generate_extension(args) -> int:
    ext_dir = Path(args.extension)
    manifest = load_extension_manifest(ext_dir)
    if manifest is None:
        logging.error("No manifest.json found in %s", ext_dir)
        return 1

    ext_name = manifest["name"]
    if manifest.get("class_registry", True) is False:
        logging.error(
            "Extension '%s' is a catalog (class_registry: false); it ships as "
            "Turtle for validation and has no generated package.",
            ext_name,
        )
        return 1
    ext_version = manifest["version"]
    display_name = manifest["display_name"]
    pkg_name = f"case-uco-{ext_name}"
    py_pkg = f"case_uco_{_sanitize_module_id(ext_name)}"

    repo_root = Path.cwd()
    ontology_dir = args.ontology_dir or repo_root / "ontology"
    output_dir = args.output_dir or repo_root / "packages" / pkg_name

    if not ontology_dir.exists():
        logging.error("Ontology directory not found: %s", ontology_dir)
        return 1

    logging.info("Parsing core ontology from %s ...", ontology_dir)
    ext_roots = [ext_dir.parent, repo_root / "extensions", repo_root / "ontology"]
    # Dedupe while preserving priority: the requested extension's own root first.
    unique_roots = list(dict.fromkeys(r.resolve() for r in ext_roots))
    schema = parse_ontology(
        ontology_dir, extensions_dir=unique_roots, include_private=frozenset({ext_dir.name})
    )

    ext_schema = _filter_extension_schema(schema, ext_name)
    if not ext_schema.classes:
        logging.warning("No SHACL-shaped classes found for extension '%s'.", ext_name)

    languages = (
        ["python", "csharp", "java", "rust"]
        if args.lang == "all"
        else [args.lang]
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    total_files = 0

    uco_compat = manifest.get("uco_compat", [])
    uco_dep = f">={uco_compat[0]}" if uco_compat else ">=1.0.0"

    for lang in languages:
        logging.info("Generating %s package for %s ...", lang, ext_name)
        count = _generate_extension_package(
            lang, ext_schema, schema, output_dir, ext_name, ext_version,
            display_name, py_pkg, uco_dep, manifest,
        )
        total_files += count
        logging.info("  -> %d files generated for %s", count, lang)

    logging.info("Generating extension registry ...")
    reg_path = _emit_extension_registry(ext_schema, schema, output_dir, ext_name)
    total_files += 1
    logging.info("  -> %s", reg_path)

    logging.info("Done: %d total files generated for extension '%s'.", total_files, ext_name)
    return 0


def _filter_extension_schema(schema, ext_name: str):
    """Extract only the classes belonging to a given extension from the full schema."""
    from case_uco_generator.schema_model import OntologySchema

    ext_prefix = f"ext.{ext_name}"
    filtered_modules = {k: v for k, v in schema.modules.items() if k.startswith(ext_prefix)}
    ext_iris = set()
    for iris in filtered_modules.values():
        ext_iris.update(iris)
    filtered_classes = {k: v for k, v in schema.classes.items() if k in ext_iris}

    return OntologySchema(
        classes=filtered_classes,
        vocabs=dict(schema.vocabs),
        namespaces=dict(schema.namespaces),
        modules=filtered_modules,
    )


def _module_display_name(module_key: str, ext_name: str) -> str:
    """Strip the internal ``ext.<name>.`` prefix from a module key.

    Internal module keys look like ``ext.cac.cacontology-sex-trafficking``;
    consumers (MCP search, language registries, documentation) expect the
    user-facing namespace prefix (``cacontology-sex-trafficking``).
    """
    expected = f"ext.{ext_name}."
    if module_key.startswith(expected):
        return module_key[len(expected):]
    return module_key


def _emit_extension_registry(ext_schema, full_schema, output_dir: Path, ext_name: str) -> Path:
    """Write _registry.json containing only the extension's classes."""
    from case_uco_generator.schema_model import iri_local_name

    module_names = sorted(
        {_module_display_name(k, ext_name) for k in ext_schema.modules.keys()}
    )

    registry: dict = {
        "extension": ext_name,
        "modules": module_names,
        "classes": {},
        "vocabs": {},
    }

    by_name: dict[str, list] = {}
    for cls in ext_schema.classes.values():
        by_name.setdefault(cls.name, []).append(cls)

    def registry_key(cls) -> str:
        # Same-named classes in different modules all stay discoverable: one
        # keeps the bare name and the rest are keyed "prefix:Name". The bare
        # name goes to the last-parsed class (the historical behaviour that
        # existing lookups rely on), except that an owl:equivalentClass alias
        # never displaces the class it aliases.
        rivals = by_name[cls.name]
        if len(rivals) == 1:
            return cls.name
        rival_iris = {r.iri for r in rivals}
        canonical = [r for r in rivals if not (rival_iris - {r.iri}).intersection(r.equivalent_iris)]
        winner = (canonical or rivals)[-1]
        return cls.name if cls is winner else f"{cls.namespace_prefix}:{cls.name}"

    py_pkg = f"case_uco_{_sanitize_module_id(ext_name)}"
    module_of = _python_extension_module_map(ext_schema, ext_name)
    for cls in sorted(ext_schema.classes.values(), key=lambda c: (c.name, c.iri)):
        all_props = full_schema.resolve_all_properties(cls)
        props_data = []
        for prop in all_props:
            props_data.append({
                "name": prop.name,
                "type": iri_local_name(prop.range_iri),
                "type_iri": prop.range_iri,
                "cardinality": prop.cardinality.value,
                "required": prop.cardinality.is_required,
                "description": prop.description,
            })
        registry["classes"][registry_key(cls)] = {
            "iri": cls.iri,
            "module": _module_display_name(cls.module, ext_name),
            "description": cls.description,
            "parents": [iri_local_name(p) for p in cls.parent_iris],
            "is_facet": cls.is_facet,
            "properties": props_data,
            "source": ext_name,
            "python_class": (
                f"{py_pkg}.{module_of[cls.iri]}."
                f"{_ext_class_name(cls.name, 'python')}"
            ),
        }

    path = output_dir / "_registry.json"
    path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def _to_snake(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def _sanitize_module_id(name: str) -> str:
    """Convert a manifest namespace prefix to a language-safe identifier.

    Manifest prefixes (e.g. ``cacontology-sex-trafficking``) contain hyphens
    that are not valid Python/C#/Java/Rust identifiers. Hyphens become
    underscores; any other non-alphanumeric character is also normalized.
    """
    sanitized = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return sanitized or "core"


def _ext_class_name(name: str, lang: str) -> str:
    from case_uco_generator.backends.base import CodegenBackend

    return CodegenBackend.safe_identifier(name, lang)


def _generate_extension_package(
    lang: str,
    ext_schema,
    full_schema,
    output_dir: Path,
    ext_name: str,
    ext_version: str,
    display_name: str,
    py_pkg: str,
    uco_dep: str,
    manifest: dict,
) -> int:
    """Generate a complete publishable package for one language.  Returns file count."""
    if lang == "python":
        return _gen_python_extension(ext_schema, full_schema, output_dir, ext_name, ext_version, display_name, py_pkg, uco_dep, manifest)
    elif lang == "csharp":
        return _gen_csharp_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep)
    elif lang == "java":
        return _gen_java_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep)
    elif lang == "rust":
        return _gen_rust_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep)
    return 0


RDFS_NAMESPACE = "http://www.w3.org/2000/01/rdf-schema#"
RDFS_LABEL = f"{RDFS_NAMESPACE}label"


@dataclasses.dataclass
class _PythonExtensionLayout:
    """Per-class decisions for a generated Python extension package."""

    modules: dict[str, list] = dataclasses.field(default_factory=dict)
    module_of: dict[str, str] = dataclasses.field(default_factory=dict)
    # class IRI -> parent OntologyClass used as the Python base (or None)
    base: dict[str, object] = dataclasses.field(default_factory=dict)
    # class IRI -> [(field_name, OntologyProperty, jsonld_key)] added over the base
    fields: dict[str, list] = dataclasses.field(default_factory=dict)
    namespace_prefix: dict[str, str] = dataclasses.field(default_factory=dict)
    typed_literal_iris: set[str] = dataclasses.field(default_factory=set)


def _python_extension_module_map(ext_schema, ext_name: str) -> dict[str, str]:
    return {
        iri: _sanitize_module_id(_module_display_name(module_key, ext_name))
        for module_key, iris in ext_schema.modules.items()
        for iri in iris
        if iri in ext_schema.classes
    }


def _python_extension_layout(ext_schema, full_schema, ext_name: str, namespaces: dict[str, str]):
    """Choose bases and fields so extension classes subclass generated core classes.

    Python keeps single inheritance like the core backend: the base is the
    first parent with a path to a CASE/UCO class (so core fields such as
    ``name`` are inherited), else the first parent generated in this package.
    Fields restated by extension shapes are emitted only when the base chain
    does not already provide them.
    """
    from case_uco_generator.backends.base import CodegenBackend
    from case_uco_generator.schema_model import (
        Cardinality,
        OntologyProperty,
        compact_ontology_iri,
        iri_local_name,
        iri_namespace,
    )

    rdfs_label = OntologyProperty(
        iri=RDFS_LABEL,
        name="label",
        range_iri="http://www.w3.org/2001/XMLSchema#string",
        range_is_class=False,
        cardinality=Cardinality.ZERO_OR_ONE,
        description="Human-readable label (rdfs:label).",
    )
    ns_to_prefix: dict[str, str] = {}
    for prefix, uri in sorted(namespaces.items()):
        ns_to_prefix.setdefault(uri, prefix)

    def jsonld_key(iri: str) -> str:
        compact = compact_ontology_iri(iri)
        if compact != iri:
            return compact
        prefix = ns_to_prefix.get(iri_namespace(iri))
        return f"{prefix}:{iri_local_name(iri)}" if prefix else iri

    def field_name(prop) -> str:
        return CodegenBackend.safe_identifier(CodegenBackend.to_snake_case(prop.name), "python")

    def is_core(cls) -> bool:
        return not cls.module.startswith("ext.")

    layout = _PythonExtensionLayout(module_of=_python_extension_module_map(ext_schema, ext_name))
    reaches_core: dict[str, bool] = {}

    def has_core_path(cls, trail: frozenset = frozenset()) -> bool:
        if is_core(cls):
            return True
        if cls.iri not in reaches_core:
            reaches_core[cls.iri] = any(
                parent is not None and has_core_path(parent, trail | {cls.iri})
                for parent in (full_schema.resolve_class(p) for p in cls.parent_iris if p not in trail)
            )
        return reaches_core[cls.iri]

    def nearest_core(cls, trail: frozenset = frozenset()):
        if is_core(cls):
            return cls
        for parent_iri in cls.parent_iris:
            parent = full_schema.resolve_class(parent_iri)
            if parent is not None and parent_iri not in trail and has_core_path(parent):
                return nearest_core(parent, trail | {cls.iri})
        return None

    def core_depth(cls) -> int:
        depth, seen = 0, set()
        while cls is not None and cls.iri not in seen:
            seen.add(cls.iri)
            depth += 1
            cls = full_schema.resolve_class(cls.parent_iris[0]) if cls.parent_iris else None
        return depth

    def choose_base(cls):
        candidates = []
        for parent_iri in cls.parent_iris:
            parent = full_schema.resolve_class(parent_iri)
            if parent is None or parent.iri == cls.iri:
                continue
            if is_core(parent) or parent.iri in layout.module_of:
                candidates.append(parent)
        # The most specific core ancestor wins (uco-identity:Organization
        # over a spine class that only reaches UcoObject); ties keep order.
        rooted = [p for p in candidates if has_core_path(p)]
        if rooted:
            return max(rooted, key=lambda p: core_depth(nearest_core(p)))
        return candidates[0] if candidates else None

    field_cache: dict[str, dict[str, str]] = {}

    def python_fields(cls, trail: frozenset = frozenset()) -> dict[str, str]:
        """Field name -> property IRI for the generated Python class of ``cls``."""
        if cls.iri in field_cache:
            return field_cache[cls.iri]
        if is_core(cls):
            parent = full_schema.resolve_class(cls.parent_iris[0]) if cls.parent_iris else None
            inherited = python_fields(parent, trail | {cls.iri}) if parent and parent.iri not in trail else {}
            result = {**inherited, **{field_name(p): p.iri for p in cls.properties}}
        else:
            base = layout.base.get(cls.iri)
            result = python_fields(base, trail | {cls.iri}) if base and base.iri not in trail else {}
            result = {**result, **{name: prop.iri for name, prop, _ in layout.fields.get(cls.iri, [])}}
        field_cache[cls.iri] = result
        return result

    ordered = sorted(ext_schema.classes.values(), key=lambda c: c.iri)
    for cls in ordered:
        layout.base[cls.iri] = choose_base(cls)

    def resolve_fields(cls, trail: frozenset = frozenset()) -> None:
        if cls.iri in layout.fields:
            return
        base = layout.base[cls.iri]
        if base is not None and not is_core(base) and base.iri not in trail:
            resolve_fields(base, trail | {cls.iri})
        inherited = python_fields(base) if base is not None else {}
        inherited_iris = set(inherited.values())
        own: list = []
        seen: set[str] = set()
        if (base is None or is_core(base)) and RDFS_LABEL not in inherited_iris:
            # Extension spines (CAC's gUFO shapes) require rdfs:label through
            # shapes in other namespaces, which property extraction skips.
            own.append(("label", rdfs_label, "rdfs:label"))
            seen.add(RDFS_LABEL)
        for prop in cls.properties:
            if prop.iri in inherited_iris or prop.iri in seen or prop.forbidden:
                continue
            seen.add(prop.iri)
            name = field_name(prop)
            key = jsonld_key(prop.iri)
            if name in inherited or any(name == n for n, _, _ in own):
                name = f"{name}_{_sanitize_module_id(key.split(':', 1)[0])}"
            own.append((name, prop, key))
            if (
                prop.is_custom_rdf_datatype
                and prop.range_iri not in full_schema.vocabs
                and not iri_local_name(prop.range_iri).endswith("Vocab")
            ):
                layout.typed_literal_iris.add(prop.iri)
        layout.fields[cls.iri] = own

    for cls in ordered:
        resolve_fields(cls)
        prefix = ns_to_prefix.get(iri_namespace(cls.iri))
        layout.namespace_prefix[cls.iri] = prefix or _module_display_name(cls.module, ext_name)
        layout.modules.setdefault(layout.module_of[cls.iri], []).append(cls)
    return layout


def _python_docstring(text: str, fallback: str) -> str:
    desc = " ".join((text or fallback).split())[:200]
    return desc.replace("\\", "\\\\").replace('"', '\\"')


def _render_python_extension_module(layout, mod_name: str, display_name: str, py_pkg: str) -> str:
    from case_uco_generator.backends.base import CodegenBackend

    def class_name(cls) -> str:
        return CodegenBackend.safe_identifier(cls.name, "python")

    classes = sorted(layout.modules[mod_name], key=lambda c: c.name)
    local = {c.iri for c in classes}
    ordered: list = []
    placed: set[str] = set()

    def place(cls) -> None:
        if cls.iri in placed:
            return
        placed.add(cls.iri)
        base = layout.base[cls.iri]
        if base is not None and base.iri in local:
            place(base)
        ordered.append(cls)

    for cls in classes:
        place(cls)

    imports: set[str] = set()

    def base_expr(base) -> str:
        if base is None:
            return ""
        if base.iri in local:
            return class_name(base)
        if not base.module.startswith("ext."):
            alias = "_" + base.module.replace(".", "_")
            imports.add(f"import case_uco.{base.module} as {alias}")
        else:
            other = layout.module_of[base.iri]
            alias = f"_{other}"
            imports.add(f"from {py_pkg} import {other} as {alias}")
        return f"{alias}.{class_name(base)}"

    body: list[str] = []
    typing_names = {"ClassVar"}
    uses_field = False
    uses_datetime = False
    uses_typed_literal = False
    for cls in ordered:
        base = base_expr(layout.base[cls.iri])
        body.append("@dataclass")
        body.append(f"class {class_name(cls)}({base}):" if base else f"class {class_name(cls)}:")
        body.append(f'    """{_python_docstring(cls.description, cls.name)}"""')
        body.append("")
        body.append(f'    CLASS_IRI: str = "{cls.iri}"')
        body.append(f'    NAMESPACE_PREFIX: str = "{layout.namespace_prefix[cls.iri]}"')
        body.append("    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES")
        for name, prop, key in layout.fields[cls.iri]:
            uses_field = True
            if prop.iri in layout.typed_literal_iris:
                type_str = "Union[str, TypedLiteral]"
                typing_names.add("Union")
                uses_typed_literal = True
            else:
                type_str = prop.type_name_for("python")
                if type_str == "Any":
                    typing_names.add("Any")
                if type_str == "datetime":
                    uses_datetime = True
            metadata = {
                "jsonld_key": key,
                "required": prop.cardinality.is_required,
                "cardinality": prop.cardinality.value,
                "range_iri": prop.range_iri,
                "alternate_range_iris": prop.alternate_range_iris,
            }
            if prop.iri in layout.typed_literal_iris:
                metadata["literal_datatype"] = True
            if prop.cardinality.is_list:
                body.append(f"    {name}: list[{type_str}] = field(default_factory=list, metadata={metadata})")
            else:
                typing_names.add("Optional")
                body.append(f"    {name}: Optional[{type_str}] = field(default=None, metadata={metadata})")
        body.append("")
        body.append("")

    header = [
        f'"""{display_name} — {mod_name} module (generated; do not edit)."""',
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass, field" if uses_field else "from dataclasses import dataclass",
    ]
    if uses_datetime:
        header.append("from datetime import datetime")
    header.append(f"from typing import {', '.join(sorted(typing_names))}")
    header.append("")
    header.extend(sorted(i for i in imports if i.startswith("import ")))
    if uses_typed_literal:
        header.append("from case_uco.typed_literal import TypedLiteral")
    header.extend(sorted({f"from {py_pkg}._context import NAMESPACES"} | {i for i in imports if i.startswith("from ")}))
    header.append("")
    names = ", ".join(f'"{class_name(c)}"' for c in classes)
    header.append(f"__all__ = [{names}]")
    header.append("")
    header.append("")
    return "\n".join(header + body).rstrip() + "\n"


def _gen_python_extension(ext_schema, full_schema, output_dir, ext_name, ext_version, display_name, py_pkg, uco_dep, manifest) -> int:
    py_dir = output_dir / "python" / py_pkg
    py_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    namespaces = {"rdfs": RDFS_NAMESPACE, **manifest.get("namespaces", {})}
    ns_lines = "\n".join(f'    "{prefix}": "{uri}",' for prefix, uri in sorted(namespaces.items()))

    layout = _python_extension_layout(ext_schema, full_schema, ext_name, namespaces)
    module_files = sorted(layout.modules)
    modules_literal = "".join(f'    "{m}",\n' for m in module_files)

    (py_dir / "_context.py").write_text(
        f'"""JSON-LD prefixes for {display_name} terms."""\n\n'
        f"NAMESPACES: dict[str, str] = {{\n{ns_lines}\n}}\n",
        encoding="utf-8",
    )
    count += 1

    init_content = (
        f'"""{display_name} — CASE/UCO SDK extension bindings.\n\n'
        "Each module holds typed dataclasses that work with ``CASEGraph.create``.\n"
        "Call :func:`register` (or ``case_uco.graph.discover_extension_class_providers()``)\n"
        'so ``CASEGraph.from_jsonld`` rehydrates these types.\n"""\n\n'
        "from __future__ import annotations\n\n"
        "import importlib\n\n"
        f"from {py_pkg}._context import NAMESPACES\n\n"
        f'__version__ = "{ext_version}"\n\n'
        f"MODULES: tuple[str, ...] = (\n{modules_literal})\n\n"
        f'# Public so the case_uco.extensions entry point (and static analysis)\n'
        f'# can reference it: the SDK registry loader resolves this at runtime.\n'
        f'REGISTRY_PATH = __file__.replace("__init__.py", "_registry.json")\n\n\n'
        "def classes() -> list[type]:\n"
        '    """Every generated class; the ``case_uco.class_registry`` provider."""\n'
        "    found: list[type] = []\n"
        "    for name in MODULES:\n"
        '        module = importlib.import_module(f"{__name__}.{name}")\n'
        "        found.extend(getattr(module, cls_name) for cls_name in module.__all__)\n"
        "    return found\n\n\n"
        "def register() -> int:\n"
        '    """Register the classes for typed ``CASEGraph.from_jsonld`` loading."""\n'
        "    from case_uco.graph import register_extension_classes\n\n"
        f'    return register_extension_classes(classes(), source="{ext_name}", context=NAMESPACES)\n\n\n'
        '__all__ = ["MODULES", "NAMESPACES", "REGISTRY_PATH", "__version__", "classes", "register"]\n'
    )
    (py_dir / "__init__.py").write_text(init_content, encoding="utf-8")
    count += 1

    for mod_name in module_files:
        source = _render_python_extension_module(layout, mod_name, display_name, py_pkg)
        (py_dir / f"{mod_name}.py").write_text(source, encoding="utf-8")
        count += 1

    pyproject = (
        "[build-system]\n"
        'requires = ["hatchling"]\n'
        'build-backend = "hatchling.build"\n\n'
        "[project]\n"
        f'name = "case-uco-{ext_name}"\n'
        f'version = "{ext_version}"\n'
        f'description = "{display_name} bindings for CASE/UCO SDK"\n'
        'requires-python = ">=3.10"\n'
        "dependencies = [\n"
        f'    "case-uco{uco_dep}",\n'
        "]\n\n"
        '[project.entry-points."case_uco.extensions"]\n'
        f'{ext_name} = "{py_pkg}:REGISTRY_PATH"\n\n'
        '[project.entry-points."case_uco.class_registry"]\n'
        f'{ext_name} = "{py_pkg}:classes"\n'
    )
    (output_dir / "python" / "pyproject.toml").write_text(pyproject, encoding="utf-8")
    count += 1
    return count


def _gen_csharp_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep) -> int:
    cs_dir = output_dir / "csharp" / f"CaseUco.{ext_name.upper()}"
    cs_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    csproj = (
        '<Project Sdk="Microsoft.NET.Sdk">\n'
        "  <PropertyGroup>\n"
        "    <TargetFramework>net8.0</TargetFramework>\n"
        f"    <PackageId>CaseUco.{ext_name.upper()}</PackageId>\n"
        f"    <Version>{ext_version}</Version>\n"
        f"    <Description>{display_name} bindings for CASE/UCO SDK</Description>\n"
        "  </PropertyGroup>\n"
        "  <ItemGroup>\n"
        f'    <PackageReference Include="CaseUco" Version="{uco_dep.lstrip(">=")}"/>\n'
        "  </ItemGroup>\n"
        "</Project>\n"
    )
    (cs_dir / f"CaseUco.{ext_name.upper()}.csproj").write_text(csproj, encoding="utf-8")
    count += 1

    for module_key, class_iris in sorted(ext_schema.modules.items()):
        parts = module_key.split(".", 2)
        prefix = parts[-1] if len(parts) > 2 else parts[-1]
        mod_name = _sanitize_module_id(prefix)
        classes = [ext_schema.classes[iri] for iri in class_iris if iri in ext_schema.classes]
        if not classes:
            continue

        ns_pascal = mod_name[0].upper() + mod_name[1:]
        lines = [
            f"// {display_name} — {mod_name} module",
            f"namespace CaseUco.Ext.{ext_name.upper()}.{ns_pascal}",
            "{",
        ]
        for cls in sorted(classes, key=lambda c: c.name):
            lines.append(f"    public class {_ext_class_name(cls.name, 'csharp')}")
            lines.append("    {")
            lines.append(f'        public static readonly string ClassIri = "{cls.iri}";')
            for prop in cls.properties:
                cs_type = prop.type_name_for("csharp")
                prop_name = prop.name[0].upper() + prop.name[1:]
                if prop.cardinality.is_list:
                    lines.append(f"        public List<{cs_type}> {prop_name} {{ get; set; }} = new();")
                else:
                    lines.append(f"        public {cs_type}? {prop_name} {{ get; set; }}")
            lines.append("    }")
            lines.append("")
        lines.append("}")

        (cs_dir / f"{ns_pascal}.cs").write_text("\n".join(lines), encoding="utf-8")
        count += 1

    return count


def _gen_java_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep) -> int:
    java_base = output_dir / "java" / "src" / "main" / "java" / "org" / "caseontology" / "ext" / ext_name
    java_base.mkdir(parents=True, exist_ok=True)
    count = 0

    pom = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<project xmlns="http://maven.apache.org/POM/4.0.0"\n'
        '         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
        '         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">\n'
        "  <modelVersion>4.0.0</modelVersion>\n"
        f"  <groupId>org.caseontology</groupId>\n"
        f"  <artifactId>case-uco-{ext_name}</artifactId>\n"
        f"  <version>{ext_version}</version>\n"
        f"  <name>{display_name}</name>\n"
        "  <dependencies>\n"
        "    <dependency>\n"
        "      <groupId>org.caseontology</groupId>\n"
        "      <artifactId>case-uco</artifactId>\n"
        f"      <version>{uco_dep.lstrip('>=')}</version>\n"
        "    </dependency>\n"
        "  </dependencies>\n"
        "</project>\n"
    )
    (output_dir / "java" / "pom.xml").write_text(pom, encoding="utf-8")
    count += 1

    for module_key, class_iris in sorted(ext_schema.modules.items()):
        parts = module_key.split(".", 2)
        prefix = parts[-1] if len(parts) > 2 else parts[-1]
        mod_name = _sanitize_module_id(prefix)
        classes = [ext_schema.classes[iri] for iri in class_iris if iri in ext_schema.classes]
        if not classes:
            continue

        for cls in sorted(classes, key=lambda c: c.name):
            lines = [
                f"package org.caseontology.ext.{ext_name}.{mod_name};",
                "",
                "import java.util.ArrayList;",
                "import java.util.List;",
                "",
                f"public class {_ext_class_name(cls.name, 'java')} {{",
                f'    public static final String CLASS_IRI = "{cls.iri}";',
                "",
            ]
            for prop in cls.properties:
                java_type = prop.type_name_for("java")
                if prop.cardinality.is_list:
                    lines.append(f"    private List<{java_type}> {prop.name} = new ArrayList<>();")
                else:
                    lines.append(f"    private {java_type} {prop.name};")
            lines.append("")
            for prop in cls.properties:
                java_type = prop.type_name_for("java")
                getter = "get" + prop.name[0].upper() + prop.name[1:]
                setter = "set" + prop.name[0].upper() + prop.name[1:]
                if prop.cardinality.is_list:
                    lines.append(f"    public List<{java_type}> {getter}() {{ return {prop.name}; }}")
                else:
                    lines.append(f"    public {java_type} {getter}() {{ return {prop.name}; }}")
                    lines.append(f"    public void {setter}({java_type} {prop.name}) {{ this.{prop.name} = {prop.name}; }}")
            lines.append("}")

            mod_dir = java_base / mod_name
            mod_dir.mkdir(parents=True, exist_ok=True)
            (mod_dir / f"{_ext_class_name(cls.name, 'java')}.java").write_text("\n".join(lines), encoding="utf-8")
            count += 1

    return count


def _gen_rust_extension(ext_schema, output_dir, ext_name, ext_version, display_name, uco_dep) -> int:
    rust_dir = output_dir / "rust" / "src"
    rust_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    cargo = (
        "[package]\n"
        f'name = "case-uco-{ext_name}"\n'
        f'version = "{ext_version}"\n'
        'edition = "2021"\n'
        f'description = "{display_name} bindings for CASE/UCO SDK"\n\n'
        "[dependencies]\n"
        f'case-uco = "{uco_dep.lstrip(">=")}"\n'
        'serde = { version = "1", features = ["derive"] }\n'
    )
    (output_dir / "rust" / "Cargo.toml").write_text(cargo, encoding="utf-8")
    count += 1

    mod_names: list[str] = []
    for module_key, class_iris in sorted(ext_schema.modules.items()):
        parts = module_key.split(".", 2)
        prefix = parts[-1] if len(parts) > 2 else parts[-1]
        mod_name = _sanitize_module_id(prefix)
        if mod_name in mod_names:
            continue
        mod_names.append(mod_name)

        classes = [ext_schema.classes[iri] for iri in class_iris if iri in ext_schema.classes]
        if not classes:
            continue

        lines = [
            f"//! {display_name} — {prefix} module\n",
            "use serde::Serialize;\n",
        ]
        for cls in sorted(classes, key=lambda c: c.name):
            desc = cls.description[:120] if cls.description else cls.name
            lines.append(f"/// {desc}")
            lines.append("#[derive(Debug, Clone, Serialize, Default)]")
            lines.append(f"pub struct {_ext_class_name(cls.name, 'rust')} {{")
            for prop in cls.properties:
                rust_type = prop.type_name_for("rust")
                field_name = _to_snake(prop.name)
                if prop.cardinality.is_list:
                    lines.append(f"    pub {field_name}: Vec<{rust_type}>,")
                else:
                    lines.append(f"    pub {field_name}: Option<{rust_type}>,")
            lines.append("}")
            lines.append("")
            lines.append(f"impl {_ext_class_name(cls.name, 'rust')} {{")
            lines.append(f'    pub fn class_iri() -> &\'static str {{ "{cls.iri}" }}')
            lines.append("}")
            lines.append("")

        (rust_dir / f"{mod_name}.rs").write_text("\n".join(lines), encoding="utf-8")
        count += 1

    lib_lines = [f"pub mod {m};" for m in mod_names]
    (rust_dir / "lib.rs").write_text("\n".join(lib_lines) + "\n", encoding="utf-8")
    count += 1

    return count


if __name__ == "__main__":
    sys.exit(main())
