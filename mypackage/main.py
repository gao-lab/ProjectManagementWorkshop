from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd

from .model import fit, predict


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--train-x", type=Path, required=True)
    parser.add_argument("--train-y", type=Path, required=True)
    parser.add_argument("--test-x", type=Path, required=True)
    parser.add_argument("--test-y", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    train_x = pd.read_csv(args.train_x, index_col=0)
    train_y = pd.read_csv(args.train_y, index_col=0)
    test_x = pd.read_csv(args.test_x, index_col=0)

    model = fit(train_x, train_y)
    test_y = predict(model, test_x)

    args.test_y.parent.mkdir(parents=True, exist_ok=True)
    test_y.to_csv(args.test_y)
