from mypackage.model import *

from .fixtures import *


def test_fit(train_x, train_y):  # Smoke test
    fit(train_x, train_y)


def test_predict(train_x, train_y, test_x, test_y):
    model = fit(train_x, train_y)
    pred_y = predict(model, test_x)
    assert (pred_y.index == test_y.index).all()
