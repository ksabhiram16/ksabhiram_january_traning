import pandas as pd

# Load dataset
df = pd.read_csv('data/titanic.csv')

# Basic info
print(df.info())
print(df.describe())