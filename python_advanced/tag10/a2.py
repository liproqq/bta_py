from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix

path = Path(__file__).parent / "data"
file_path = path / "house-flat-office.txt"
df = pd.read_csv(file_path, sep="\t")

coldic = {"Wohnung": "k", "Haus": "r", "Buero": "b"}
df["Color"] = df["Kategorie"].map(coldic)

features = df.columns[:len(df.columns)-2].values

scaler = MinMaxScaler()
df_n = df[features].copy()

df_n[features] = scaler.fit_transform(df[features])

fig = plt.figure()
graph3d = fig.add_subplot(121, projection='3d')
graph3d.scatter(df['Quadratmeter'],
                df['Wandhoehe'],
                df['IA_Ratio'],
                color=df['Color'])
graph3d.set_xlabel('Quadratmeter')
graph3d.set_ylabel('Wandhoehe')
graph3d.set_zlabel('IA_Ratio')

graph3d2 = fig.add_subplot(122, projection='3d')
graph3d2.scatter(df_n['Quadratmeter'],
                 df_n['Wandhoehe'],
                 df_n['IA_Ratio'],
                 color=df['Color'])
graph3d2.set_xlabel('Quadratmeter')
graph3d2.set_ylabel('Wandhoehe')
graph3d2.set_zlabel('IA_Ratio')
graph3d2.set_xlim(left=0)
graph3d2.set_ylim(bottom=0)
graph3d2.set_zlim(bottom=0)
plt.show()
