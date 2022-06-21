import pandas as pd

df = pd.read_csv("dane2.csv")

print(df)
print(df.describe())
# generowanie wykresów
df.plot(kind="bar")
