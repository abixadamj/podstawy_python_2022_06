import pandas as pd


def read_from_xlsx(file_name):
    """read Excel, return DataFrame"""
    try:
        df = pd.read_excel(file_name)
        return (True, df)  # zwracamy 2 wartości - Tupla
    except:
        return (False, False)


def write_df_to_xlsx(df_to_write, file_name):
    """read DataFrame, write Excel"""
    try:
        df_to_write.to_excel(file_name, engine="openpyxl")
        return True
    except:
        return False

def split_to_xlsx(df, selected_owner, column_name="Owner Org"):
    """split our df to many dfs"""
    unique_owners = df[column_name].unique()
    # zamiana NDArray na listę zwykłą: metoda tolist()
    unique_owners = unique_owners.tolist()
    info = None
    for owner in unique_owners:
        df_owner = owner.replace(" ", "_")
        xlsx_file_name = f"{df_owner}.xlsx"
        df_temporary = df.loc[df[column_name] == owner]
        write_df_to_xlsx(df_temporary, xlsx_file_name)
        if owner == selected_owner:
            info = "Ważne informacje"

    return info
