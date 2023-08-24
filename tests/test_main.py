from subprocess import run
from .fixtures import *

def test_main(train_x, train_y, test_x, tmp_path):
    train_x.to_csv(tmp_path / "train_x.csv")
    train_y.to_csv(tmp_path / "train_y.csv")
    test_x.to_csv(tmp_path / "test_x.csv")
    run(
        [
            "mypackage",
            "--train-x",
            tmp_path / "train_x.csv",
            "--train-y",
            tmp_path / "train_y.csv",
            "--test-x",
            tmp_path / "test_x.csv",
            "--test-y",
            tmp_path / "test_y.csv",
        ]
    )
    assert (tmp_path / "test_y.csv").is_file()
