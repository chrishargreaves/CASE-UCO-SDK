# SOLVE-IT worked example — laptop acquisition

Synthetic (Tier T0) worked example behind
`docs/recipes/solve-it-investigation-planning.md`: a seized laptop SSD is
imaged and hash-verified, with every step documented against the
[SOLVE-IT](https://solveit-df.org) knowledge base vendored in
`ontology/solveit/`.

What it demonstrates:

- Stating the investigation objective (DFO-1006 "Acquire data").
- Recording the acquisition as a `solveit-core:SolveitInvestigativeAction`
  that is also typed with the knowledge-base technique class DFT-1002 (a
  `uco-action:Technique`; SOLVE-IT 0.2.x deprecated `usedTechnique`), with
  `appliedMitigation` (DFM-1003, DFM-1004) pointing at canonical IRIs.
- SOLVE-IT observables: `PhysicalImageContainer` containing a `Bitstream`,
  plus a `HashVerificationResult`.
- Error Mitigation Analysis: risk-rating weakness DFW-1004 with
  `solveit-wa:WeaknessEvaluation` (likelihood x impact).
- The same metaclass pattern on a plain `uco-action:Action` typed with
  `solveit-data:techniqueDFT-1042`.

Rebuild and validate:

```bash
.venv/bin/python examples/solveit/build_laptop_acquisition_solveit.py
```

The builder writes `laptop-acquisition-solveit.jsonld` and runs
`case_validate` with `extensions=["solveit"]` (must conform).
