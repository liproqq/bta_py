from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import plot_confusion_matrix, accuracy_score
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)

features = data.data
target = data.target
names = data.target_names

sepal_cols = ["sepal length (cm)", "sepal width (cm)"]
petal_cols = ["petal length (cm)", "petal width (cm)"]

# split
(X_sepal_train, X_sepal_test,
 y_sepal_train, y_sepal_test) = train_test_split(features[sepal_cols], target,
                                                 train_size=.8,
                                                 random_state=42)
(X_petal_train, X_petal_test,
 y_petal_train, y_petal_test) = train_test_split(features[petal_cols], target,
                                                 train_size=.8,
                                                 random_state=42)
X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                    train_size=.8,
                                                    random_state=42)

# instantiate knn models
knn_sepal = KNeighborsClassifier(n_neighbors=5)
knn_petal = KNeighborsClassifier(n_neighbors=5)
knn = KNeighborsClassifier(n_neighbors=5)

# fit models
knn_sepal.fit(X_sepal_train, y_sepal_train)
knn_petal.fit(X_petal_train, y_petal_train)
knn.fit(X_train, y_train)

# predict
y_sepal_predict = knn_sepal.predict(X_sepal_test)
y_petal_predict = knn_petal.predict(X_petal_test)
y_predict = knn.predict(X_test)

# get scores
print(accuracy_score(y_sepal_test, y_sepal_predict))
print(accuracy_score(y_petal_test, y_petal_predict))
print(accuracy_score(y_test, y_predict))

# plot low score
plot_confusion_matrix(knn_sepal, X_sepal_test, y_sepal_test, normalize="true")
plt.show()
