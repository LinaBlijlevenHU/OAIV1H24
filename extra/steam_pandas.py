import pandas as pd

df = pd.read_json("../steam.json")

print(df.describe())
print(df.info())
print(df.head())