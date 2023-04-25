from snakemake.remote.HTTP import RemoteProvider as HTTPRemoteProvider

HTTP = HTTPRemoteProvider()


container: "continuumio/miniconda3:4.8.2"


rule prepare:
    input:
        HTTP.remote(
            "https://microdata.epi.org/epi_cpsbasic_2000_2023.zip", keep_local=True
        ),
    output:
        "results/prepared.parquet",
    conda:
        "envs/pandas.yaml"
    script:
        "scripts/prepare.py"


rule households:
    input:
        *rules.prepare.output,
    output:
        "results/households.parquet",
    conda:
        "envs/pandas.yaml"
    script:
        "scripts/households.py"


rule metadata:
    input:
        *rules.prepare.output,
    output:
        "results/meta.json",
    conda:
        "envs/pandas.yaml"
    script:
        "scripts/metadata.py"


rule all:
    default_target: True
    input:
        *rules.prepare.output,
        *rules.households.output,
        *rules.metadata.output,
