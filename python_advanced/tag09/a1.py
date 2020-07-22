from pathlib import Path
import pandas as pd
import numpy as np

path = Path(__file__).parent / "data"

df = pd.read_csv(path / "cars.csv",
                 usecols=['num-of-cylinders', 'horsepower',
                          'peak-rpm', 'city-mpg', 'highway-mpg', 'price'],
                 na_values="?")

df["num-of-cylinders"] = df["num-of-cylinders"].map({'four': 4, 'six': 6,
                                                     'five': 5, 'three': 3,
                                                     'twelve': 12, 'two': 2,
                                                     'eight': 8})

# ['horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg']

cols = ['horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg']

b_final = (df["num-of-cylinders"] == 4) & ((df["city-mpg"] == 23) |
                                           (df["highway-mpg"] == 31))

print(df[b_final][cols].describe())
print(df[b_final][cols].mode())
