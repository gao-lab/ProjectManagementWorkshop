import numpy as np
import pandas as pd
from pytest import fixture


@fixture
def train_x() -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(50, 5))


@fixture
def train_y() -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(50, 1))


@fixture
def test_x() -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(10, 5))


@fixture
def test_y() -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(10, 1))
