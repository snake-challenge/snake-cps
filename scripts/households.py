import pandas as pd

sm = snakemake  # noqa

df = pd.read_parquet(sm.input[0])

hh_size = df.groupby(["hhid", "year", "month"]).size().sort_values(ascending=False)

mask_hh_big = hh_size.index.get_level_values("hhid").duplicated(keep="first")
hh_idx = hh_size.index[~mask_hh_big]

hh = df.loc[hh_idx].droplevel(["year", "month"]).sort_index()

hh.to_parquet(sm.output[0])
