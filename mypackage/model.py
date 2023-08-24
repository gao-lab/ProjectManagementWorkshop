import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def fit(x: pd.DataFrame, y: pd.DataFrame) -> RandomForestRegressor:
    r"""
    Fit a random forest regression model on training data

    Parameters
    ----------
    x
        Training input
    y
        Training output

    Returns
    -------
    model
        Fitted regression model
    """
    model = RandomForestRegressor()
    model.fit(x, y.iloc[:, 0].ravel())
    return model


def predict(model: RandomForestRegressor, x: pd.DataFrame) -> pd.DataFrame:
    r"""
    Use a fitted model to predict on test data

    Parameters
    ----------
    model
        Fitted regression model
    x
        Testing input

    Returns
    -------
    y
        Testing output
    """
    y = model.predict(x)
    y = pd.DataFrame(y, index=x.index)
    return y
