from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import plot_confusion_matrix, accuracy_score

path = Path(__file__).parent.parent / "tag10" / "data"
file_path = path / "house-flat-office.txt"
df = pd.read_csv(file_path, sep="\t", index_col="Immobilie")

feat_cols = ["Quadratmeter", "Wandhoehe", "IA_Ratio"]

X = df[feat_cols].copy()
y = df["Kategorie"]

scaler = MinMaxScaler()
X[feat_cols] = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    train_size=.8,
                                                    random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(pd.crosstab(y_test, y_pred, rownames=["True"], colnames=["Pred"]))

plot_confusion_matrix(knn, X_test, y_test, normalize="true")
plt.show()
