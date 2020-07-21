import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"

astro = pd.read_csv(path / "astronauts.csv", usecols=["Space Flights",
                                                      "Space Flight (hr)",
                                                      "Space Walks",
                                                      "Space Walks (hr)"])

print(astro.apply('mean'))

# print(astro[["Space Flights",
#              "Space Flight (hr)",
#              "Space Walks",
#              "Space Walks (hr)"]].mean())
