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

print(target)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.scatter(features.iloc[:, 0], features.iloc[:, 1], c=target)
ax1.set_xlabel("sepal width")
ax1.set_ylabel("sepal length")

ax2 = fig.add_subplot(122)
ax2.scatter(features.iloc[:, 2], features.iloc[:, 3], c=target)
ax2.set_xlabel("petal width")
ax2.set_ylabel("petal length")

# plt.show()
