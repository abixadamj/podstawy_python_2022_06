import pandas as pd

df = pd.read_excel("db_test.xlsx")
# ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
print(df)
print(df.info())

df_global_bus = df.loc[df["Owner Org"] == 'Global Business']
df_detail = df.loc[df["Owner Org"] == 'Detail']

unique_owners = df["Owner Org"].unique()
# zamiana NDArray na listę zwykłą: metoda tolist()
unique_owners = unique_owners.tolist()
print(type(unique_owners))
df_owners = {}

for owner in unique_owners:
    df_owner = owner.replace(" ", "_")
    # df_owner = df_owner.replace("P", "*")
    print(f"Make new df for {owner} -> {df_owner}")
    df_owners[df_owner] = df.loc[df["Owner Org"] == owner]

print(df_owners)
