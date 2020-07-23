from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix

path = Path(__file__).parent / "data"
file_path = path / "house-flat-office.txt"
df = pd.read_csv(file_path, sep="\t", index_col="Immobilie")

coldic = {"Wohnung": "k", "Haus": "r", "Buero": "b"}
df["Color"] = df["Kategorie"].map(coldic)

features = df.columns[:len(df.columns)-2].values

scaler = MinMaxScaler()
df_n = df[features].copy()

df_n[features] = scaler.fit_transform(df[features])

X_train, X_test, y_train, y_test = train_test_split(df_n,
                                                    df["Kategorie"],
                                                    train_size=.8,
                                                    random_state=42)


def knn(k=5, X_train=X_train, y_train=y_train, X_test=X_test):
    y_pred = []

    for _, row in X_test.iterrows():
        y_temp = X_train - row
        y_temp = y_temp.pow(2)
        y_temp = y_temp.sum(axis=1)
        y_temp = y_temp.map(np.sqrt)
        y_temp = y_temp.sort_values()[:k]
        y_temp = y_train.loc[y_temp.index]
        y_temp = y_temp.mode()[0]

        y_pred.append(y_temp)
    return np.array(y_pred)


y_pred = knn()
y_true = y_test.values

# print(confusion_matrix(y_true, y_pred))
print(pd.crosstab(y_test,
                  y_pred,
                  rownames=["True"],
                  colnames=["Pred"]))
