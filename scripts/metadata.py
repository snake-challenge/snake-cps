import json

import pandas as pd

sm = snakemake  # noqa

df = pd.read_parquet(sm.input[0])

metadata = [
    {
        "name": label,
        "type": (
            "finite/ordered"
            if (not s.dtype == "category") or s.cat.ordered
            else "finite"
        ),
        "representation": (
            s.cat.categories.tolist()
            if s.dtype == "category"
            else list(map(str, range(s.min(), s.max() + 1)))
        ),
    }
    for label, s in df.items()
]

with open(sm.output[0], "w") as f:
    json.dump(metadata, f)
