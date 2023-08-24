from pathlib import Path

import pandas as pd


df = pd.read_csv("iris.csv")
df["species"] = df["species"].astype("category").cat.codes
x = df.iloc[:, 1:].astype(float)
y = df.iloc[:, 0].astype(float)

path = Path("../../processed/iris")
path.mkdir(parents=True, exist_ok=True)
x.to_csv(path / "x.csv")
y.to_csv(path / "y.csv")

