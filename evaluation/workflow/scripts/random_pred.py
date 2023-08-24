from argparse import ArgumentParser, Namespace
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--train-x", type=Path, required=True)
    parser.add_argument("--train-y", type=Path, required=True)
    parser.add_argument("--test-x", type=Path, required=True)
    parser.add_argument("--test-y", type=Path, required=True)
    return parser.parse_args()


def main(args: Namespace) -> None:
    train_y = pd.read_csv(args.train_y, index_col=0)
    test_x = pd.read_csv(args.test_x, index_col=0)
    mean, std = train_y.mean().iloc[0], train_y.std().iloc[0]
    test_y = pd.DataFrame(
        np.random.randn(test_x.shape[0]) * std + mean,
        index=test_x.index,
    )
    args.test_y.parent.mkdir(parents=True, exist_ok=True)
    test_y.to_csv(args.test_y)


if __name__ == "__main__":
    main(parse_args())
