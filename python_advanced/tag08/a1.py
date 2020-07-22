import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"

abb = pd.read_csv(path / "state-abbrevs.csv")
area = pd.read_csv(path / "state-areas.csv")
pop = pd.read_csv(path / "state-population.csv")

df = pd.merge(abb, pop,
              left_on="abbreviation", right_on="state/region",
              validate="1:m", how="outer")

# for df in (abb, area, pop):
#     print(df.head(), "\n")

print(df.isna().any())

df.loc[df["state/region"] == "PR", ["state"]] = "Puerto Rico"

df.loc[:, ["state", "state/region"]] =\
    df.loc[:, ["state", "state/region"]].fillna(axis=1, method="bfill")

df = df.drop("abbreviation", axis=1)

# print(df[df["population"].isna()])

df = df.dropna(axis=0)
df = pd.merge(df, area,
              validate="m:1", how="outer")

df = df.fillna(area["area (sq. mi)"].sum())


df[["population", "area (sq. mi)"]] =\
    df[["population", "area (sq. mi)"]].astype(int)

print(df)
print(df.notnull().any())

df.to_csv(path / "final.csv", index=False)