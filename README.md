# SNAKE CPS

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7861403.svg)](https://doi.org/10.5281/zenodo.7861403)
[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:10aabffde6f5a50ecc81c631b3f42beaa2b5aa9d/)](https://archive.softwareheritage.org/swh:1:dir:10aabffde6f5a50ecc81c631b3f42beaa2b5aa9d;origin=https://github.com/snake-challenge/snake-cps;visit=swh:1:snp:0b29db053816a71f4071dd6a593efafbfd311967;anchor=swh:1:rev:0b0fd5a4c287a5c25517bfd6af94cd02f47ee869)

## Usage

```console
snakemake --use-conda
```

## Description

Adapted from EPI CPS Basic Monthly data provided by the Economic Policy Institute [^1].

Available features are:

|           | age      | agechild | citistat | female | married | ownchild | wbhaom | gradeatn | cow1 | ftptstat | statefips | hoursut  | faminc | mind16 | mocc10 |
|-----------|----------|----------|----------|--------|---------|----------|--------|----------|------|----------|-----------|----------|--------|--------|--------|
| Numerical | X        |          |          |        |         | X        |        |          |      |          |           | X        |        |        |        |
| Ordinal   | X        |          |          |        |         | X        |        | X        |      |          |           | X        | X      |        |        |
| Unique    | 65       | 16       | 5        | 2      | 2       | 12       | 6      | 16       | 8    | 9        | 51        | 129      | 15     | 16     | 10     |
| Range     | [16, 80] |          |          |        |         | [0, 11]  |        |          |      |          |           | [0, 198] |        |        |        |

Description is available at https://microdata.epi.org/variables/.
Categorical variables are encoded as Pandas Categoricals and ordered when appropriate.
`results/meta.json` is the table schema
in [TAPAS format](https://privacy-sdg-toolbox.readthedocs.io/en/latest/dataset-schema.html).

Records with missing values, `faminc <= 0`, `age < 16`, or `basicwgt <= 0` are dropped.
Only the years 2005 to 2022 are used due to consistency issues.

Combinaison `hhid`, `year`, `month` is used as index and we *assume* households linkability.

`results/households.parquet` is indexed with `hhid` only and contains each household once, retaining the `year`, `month` with
its
largest number of records.

[^1]: Economic Policy Institute. 2023. Current Population Survey Extracts, Version 1.0.39, https://microdata.epi.org.
