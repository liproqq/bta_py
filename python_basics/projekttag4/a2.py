from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


baby_names_file = Path(__file__).parent / "data/Popular_Baby_Names.csv"

df = pd.read_csv(baby_names_file)

to_repl = df[df["Year of Birth"] == 2012]["Ethnicity"].unique()

repl_with = df[df["Year of Birth"] != 2012]["Ethnicity"].unique()

for i in range(len(to_repl)):
    b_series = df['Ethnicity'] == to_repl[i]
    df.loc[b_series, 'Ethnicity'] = repl_with[i]


print("Aufgabe 1:", df["Year of Birth"].unique())

print("Aufgabe 2:", df.groupby("Year of Birth")["Count"].sum())

print("Aufgabe 3:", df.groupby(["Year of Birth", "Gender"])["Count"].sum())

plt.plot(df.groupby("Year of Birth")["Count"].sum())
plt.ylim(0, 150000)
plt.show()
