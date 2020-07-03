from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent.joinpath("data")

astronauts_file = Path(data_path).joinpath("astronauts.csv")

df = pd.read_csv()

print(df.head())