import pandas as pd
import yaml
from parse import parse
from snakemake.script import Snakemake

PATTERN = "results/{dataset}/{method}/metrics.yaml"


def main(snakemake: Snakemake) -> None:
    df = []
    for item in snakemake.input:
        conf = parse(PATTERN, item).named
        with open(item) as f:
            content = yaml.load(f, Loader=yaml.Loader)
        df.append({**conf, **content})
    sort_order = list(conf.keys())
    df = pd.DataFrame.from_records(df).sort_values(sort_order)
    df.to_csv(snakemake.output[0], index=False)


if __name__ == "__main__":
    main(snakemake)  # noqa: F821  # pyright: ignore[reportUndefinedVariable]
