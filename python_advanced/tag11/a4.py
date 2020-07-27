from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, mean_squared_error

cars_file = Path(__file__).parent / "data/cleancars.csv"

df = pd.read_csv(cars_file)

# pd.plotting.scatter_matrix(df, c=df["price"], cmap="gist_heat")
# plt.show()

features = df[["horsepower"]]
target = df["price"]

X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                    train_size=.8,
                                                    random_state=42)

lr = LinearRegression(normalize=True)

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)


# x_axis = np.linspace(features.min(), features.max())
# y_axis = lr.coef_*x_axis + lr.intercept_
# plt.scatter(features, target, c=target)
# plt.plot(x_axis, y_axis, color="r")
# plt.show()

print(lr.score(X_train, y_train))
print(lr.score(X_test, y_test))
