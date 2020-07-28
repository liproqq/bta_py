import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def plot_data(X, y, kernel='linear', degree=2, C=1):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42)

    # Erstellen des Vektorraumes
    svm = SVC(kernel=kernel, C=C, degree=degree)
    svm.fit(X_train, y_train)

    # Zur darstellung der Vektorräume
    x = X['petal length (cm)']
    y = X['petal width (cm)']

    # Meshgrid
    xx, yy = np.meshgrid(np.linspace(x.min()-1, x.max()+1, 100),
                         np.linspace(y.min()-1, y.max()+1, 100))

    # print(xx.shape)
    # print(xx.ravel().shape)
    # print(xx[0])
    # print(yy.shape)
    # print(yy[0])

    X_mesh = pd.DataFrame({'petal length (cm)': xx.ravel(),
                           'petal width (cm)': yy.ravel()})
    # print(X_mesh)

    Z = svm.predict(X_mesh)
    Z = Z.reshape(xx.shape)
    # print(Z)

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.contourf(xx, yy, Z, cmap='summer')
    ax.scatter(X_train['petal length (cm)'],
               X_train['petal width (cm)'],
               c=y_train,
               cmap='summer',
               edgecolors='k',
               label='Train')
    ax.scatter(X_test['petal length (cm)'],
               X_test['petal width (cm)'],
               c=y_test,
               cmap='summer',
               edgecolors='r',
               marker='D',
               s=30,
               label='Test')
    ax.legend()
    ax.set_title(f'Kernel={kernel}, C={C}, degree={degree}')
    plt.show(block=False)

data = load_iris(as_frame=True)

features = data.data[['petal length (cm)', 'petal width (cm)']]
target = data.target
names = data.target_names

print(features)
print(target)
print(names)

plot_data(features, target)
plot_data(features, target, kernel='poly')
plot_data(features, target, kernel='poly', degree=3)
plot_data(features, target, kernel='poly', degree=4)
plot_data(features, target, kernel='poly', degree=5)
plot_data(features, target, kernel='poly', degree=5, C=100)
plot_data(features, target, kernel='rbf')
plot_data(features, target, kernel='rbf', C=100)

# plt.scatter(features.iloc[:, 0], features.iloc[:, 1], c=target)
# plt.xlabel('petal length (cm)')
# plt.ylabel('petal width (cm)')
# plt.show()
input()
