import pandas as pd
from sklearn.datasets import load_iris

df = load_iris(as_frame=True).frame

print(df["target"].unique())
