import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
from mpl_toolkits.mplot3d import Axes3D

centers = [[1, 1], [1, 12], [12, 1]]

X, _ = make_blobs(n_samples=500, centers=centers, cluster_std=1)

# plt.scatter(X[:, 0], X[:, 1])
# plt.show()

ms = MeanShift()
ms.fit(X)

y_pred = ms.labels_
centers_pred = ms.cluster_centers_

print(centers_pred)
print(y_pred)

plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
