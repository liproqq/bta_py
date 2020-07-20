import pandas as pd


df1 = pd.DataFrame({'mitarbeiter': ['Lisa', 'Sue', 'Larry', 'Jane'],
                    'dep': ['Dev', 'PR', 'PR', 'HR']})
df2 = pd.DataFrame({'employee': ['Larry', 'Bob', 'Jane', 'Sue'],
                    'salary': [2000, 2500, 3000, 4000]})

df = pd.merge(df1, df2, how="outer",
              left_on="mitarbeiter",
              right_on="employee",
              validate="m:1")


df.loc[df["mitarbeiter"].isna(), "mitarbeiter"] = df["employee"]

df.drop("employee", inplace=True, axis=1)

print(df1)
print(df2)
print(df)
