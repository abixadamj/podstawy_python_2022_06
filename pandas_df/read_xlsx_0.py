import pandas as pd

df = pd.read_excel("db_test.xlsx")
# w Linuksie: ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.

print(df.head())
print(df.info())

# owner Org
print(df["Owner Org"].unique())
# recznie tworzymy jedną df
df_global_bus = df.loc[df["Owner Org"] == 'Global Business']
print(df_global_bus)

# a teraz zrobimy automat, który stworzy odpowiednią ilość df....
# oraz aplikacja desktopowa w PySimpleGUI
