import pandas as pd
print("pandas loaded")


df = pd.read_excel("test.xlsx,train.xlsx")
df.drop(columns=['Order ID', 'Order Date'], inplace=True)
df