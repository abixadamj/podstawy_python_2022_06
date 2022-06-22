import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dane2.csv")
print(df)
print(df.describe())
# generowanie wykresów
df[["Name", "Outcome"]].plot(kind="bar")
plt.savefig("demo.png")
