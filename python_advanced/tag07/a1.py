from pathlib import Path
import pandas as pd
import numpy as np

path = Path(__file__).parent
data_path = path / "data/"

df14 = pd.read_csv(data_path/"EU2014_BE_EndgErg_Wahlbezirke.csv",
                   encoding="cp1252", sep=";")[["Wahlbezirk",
                                                "Waehler",
                                                "CDU",
                                                "GRÜNE",
                                                "SPD"]].dropna()
df19 = pd.read_csv(data_path/"EU2019_BE_EndgErg_Wahlbezirke.csv",
                   encoding="cp1252", sep=";")[["Wahlbezirk",
                                                "Wähler",
                                                "CDU",
                                                "GRÜNE",
                                                "SPD"]].dropna()

df19["Wähler"] = df19["Wähler"].str.replace(" ", "")

df14["Wähler"] = df14["Waehler"]
df14.drop("Waehler", inplace=True, axis=1)

df19[["Wähler", "CDU", "GRÜNE", "SPD"]] = df19[["Wähler",
                                                "CDU",
                                                "GRÜNE",
                                                "SPD"]].astype(int)

df = pd.merge(df14, df19, left_index=True, right_index=True,
              suffixes=("_14", "_19"), how="outer", sort=True)

df = df[sorted(df.columns)]


print(df.info())