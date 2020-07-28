from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

cars_file = Path(__file__).parent.parent / "tag11/data/cleancars.csv"

df = pd.read_csv(cars_file)

features = df[["horsepower"]]
target = df["highway-mpg"]

X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                    train_size=.8,
                                                    random_state=100)

lr = LinearRegression(normalize=True)

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# x_axis = np.linspace(features.min(), features.max())
# y_axis = lr.coef_*x_axis + lr.intercept_
# plt.scatter(X_train["horsepower"], y_train)
# plt.scatter(X_test["horsepower"], y_test)
# plt.plot(x_axis, y_axis, color="r")
# plt.show()


poli = PolynomialFeatures(degree=3)

X_train_poli = poli.fit_transform(X_train)
X_test_poli = poli.transform(X_test)

pr = LinearRegression()

pr.fit(X_train_poli, y_train)

x_poli = np.linspace(features.min(), features.max())
x_poli = poli.transform(x_poli)
poli_reg_graph = pr.predict(x_poli)

# print(pr.coef_, pr.intercept_)
print(lr.score(X_train, y_train))
print(lr.score(X_test, y_test))
print(pr.score(X_train_poli, y_train))
print(pr.score(X_test_poli, y_test))

x_axis = np.linspace(features.min(), features.max())
y_axis = lr.coef_*x_axis + lr.intercept_
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test)
plt.plot(x_axis, y_axis, color="r")
plt.plot(x_axis, poli_reg_graph, color="b")
plt.show()
