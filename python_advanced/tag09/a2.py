import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path = os.path.join(os.path.dirname(__file__), 'data')
df = pd.read_csv(os.path.join(path, 'cleancars.csv'))

# print(df.describe())

# df.boxplot(column="price")

# df.plot(x="horsepower", y="peak-rpm", kind="scatter")

# pd.plotting.scatter_matrix(df, diagonal="kde")

print(df.groupby("num-of-cylinders")["price"].describe())

print(df.groupby("num-of-cylinders")["price"].mean())

df.groupby("num-of-cylinders")["price"].mean().plot.bar()

plt.show()
