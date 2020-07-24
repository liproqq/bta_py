import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

path = Path(__file__).parent

df = pd.read_csv(path / "avocado-unclean.csv")

# print(df["Unnamed: 0"].unique())

df = df.drop(columns="Unnamed: 0")

# print(df["region"].unique())

df["region"][df["region"].str.lower() == "albany"] = "Albany"

# print(df["region"].unique())
# print(df.head())

# print(df.shape)

df = df[~df.duplicated()]

# print(df.shape)

# print(df.isnull().any())

df["year"] = pd.to_datetime(df["Date"]).dt.year

# print(df.isnull().any())
# print(df["year"].unique())

# print(df.info())

# print(df[df["Total Volume"] == df[["S", "L", "XL"]].sum(axis=1)])
# print(df[df["Total Bags"] == df[["Small Bags",
#                                  "Large Bags",
#                                  "XLarge Bags"]].sum(axis=1)])

df["Total Volume"] = df[["S", "L", "XL"]].sum(axis=1)

# print(df[df["Total Volume"] == df[["S", "L", "XL"]
#                                    ].sum(axis=1)].notnull().all())
df["Total Bags"] = df[["Small Bags", "Large Bags", "XLarge Bags"]].sum(axis=1)
# print(df[df["Total Bags"] == df[["Small Bags",
#                                  "Large Bags",
#                                  "XLarge Bags"]
#                                  ].sum(axis=1)].notnull().all())


df["Revenue"] = df["AveragePrice"]*df["Total Volume"]

print(df.groupby(["year", "type"])["Revenue"].sum().unstack("type"))

df.groupby(["year", "type"])["Revenue"].sum().unstack("type").plot.bar()

plt.show()
