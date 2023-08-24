from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd
import yaml
from sklearn.metrics import mean_squared_error, r2_score


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--true", type=Path, required=True)
    parser.add_argument("--pred", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main(args: Namespace) -> None:
    true = pd.read_csv(args.true, index_col=0)
    pred = pd.read_csv(args.pred, index_col=0)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        yaml.dump(
            {
                "r2": r2_score(true, pred).item(),
                "mse": mean_squared_error(true, pred).item(),
            },
            f,
        )


if __name__ == "__main__":
    main(parse_args())
