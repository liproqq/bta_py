from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent.joinpath("data")

astronauts_file = Path(data_path).joinpath("astronauts.csv")

df = pd.read_csv(astronauts_file)

print(df[(df["Gender"] == "Male") & (df["Space Walks"] > 2)][["Name", "Gender", "Space Walks"]])

# for row in df.iterrows():
#     print(row)