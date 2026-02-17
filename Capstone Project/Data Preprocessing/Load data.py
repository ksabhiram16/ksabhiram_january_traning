import pandas as pd

df = pd.read_csv("data/raw/your_dataset.csv")
print(df.head())
print(df.info())
print(df.describe())
