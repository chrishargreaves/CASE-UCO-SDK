# CAC T0 fixtures

Synthetic graphs for named CAC validation subsets. Names, times, and
locations are fabricated.

| File | Profile | Purpose |
| --- | --- | --- |
| `t0-missing-child.jsonld` | `cac:missing-child` | Conforming missing-child / case-initiation fixture |
| `t0-missing-child-invented-term.jsonld` | `cac:missing-child` | Negative fixture: invented CAC class |

```python
from case_uco.validation import validate_graph_file

report = validate_graph_file(
    "examples/cac/t0-missing-child.jsonld",
    extensions=["cac:missing-child"],
)
assert report.conforms
```

Requires case-utils 0.18.0 and `--built-version case-1.5.0` (CASE/UCO 1.5.0, CAC 3.1.0).
