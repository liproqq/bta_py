from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = Path(__file__).parent / "data"
file_path = path / "house-flat-office.txt"

df = pd.read_csv(file_path, sep="\t", index_col=0)

# print(df.info())
# print(df.groupby("Kategorie").agg(["min", "max", "mean", "std"]))

df["Color"] = df["Kategorie"].map({"Haus": "r",
                                   "Wohnung": "k",
                                   "Buero": "b"})

cols = ["Quadratmeter", "Wandhoehe", "IA_Ratio"]

# pd.plotting.scatter_matrix(df[cols], c=df["Color"], s=30)
# plt.show()

fig = plt.figure()
graph3d = fig.add_subplot(111, projection="3d")
graph3d.scatter(df["Quadratmeter"],
                df["Wandhoehe"],
                df["IA_Ratio"],
                color=df["Color"])
graph3d.set_xlabel("Quadratmeter")
graph3d.set_ylabel("Wandhoehe")
graph3d.set_zlabel("IA_Ratio")
graph3d.set_xlim(left=0)
graph3d.set_ylim(bottom=0)
graph3d.set_zlim(bottom=0)

plt.show()
