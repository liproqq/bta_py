import pandas as pd

df1 = pd.DataFrame({"Name": ["Schmitt", "Müller", "Meier"],
                    "Adresse": ["Hauptstraße 3",
                                "Am Berg 2",
                                "Weg 4"]})

df2 = pd.DataFrame({"Vorname": ["Hellen", "Erna", "Johann"],
                    "Nachname": ["Schmitt", "Müller", "Meyer"]})

df = pd.merge(df1, df2, left_on="Name", right_on="Nachname")
df.drop("Name", axis=1, inplace=True)

print(df)
