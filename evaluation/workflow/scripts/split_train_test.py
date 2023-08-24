from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--input-x", type=Path, required=True)
    parser.add_argument("--input-y", type=Path, required=True)
    parser.add_argument("--output-train-x", type=Path, required=True)
    parser.add_argument("--output-train-y", type=Path, required=True)
    parser.add_argument("--output-test-x", type=Path, required=True)
    parser.add_argument("--output-test-y", type=Path, required=True)
    return parser.parse_args()


def main(args: Namespace) -> None:
    x = pd.read_csv(args.input_x, index_col=0)
    y = pd.read_csv(args.input_y, index_col=0)

    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)

    args.output_train_x.parent.mkdir(parents=True, exist_ok=True)
    args.output_train_y.parent.mkdir(parents=True, exist_ok=True)
    args.output_test_x.parent.mkdir(parents=True, exist_ok=True)
    args.output_test_y.parent.mkdir(parents=True, exist_ok=True)

    train_x.to_csv(args.output_train_x)
    train_y.to_csv(args.output_train_y)
    test_x.to_csv(args.output_test_x)
    test_y.to_csv(args.output_test_y)


if __name__ == "__main__":
    main(parse_args())
