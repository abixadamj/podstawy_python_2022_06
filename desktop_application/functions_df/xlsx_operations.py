import pandas as pd
import os


def read_from_xlsx(file_name):
    """read Excel, return DataFrame"""
    _, extension = os.path.splitext(file_name)
    if extension.lower() != ".xlsx":  # != różne
        return False, f"{extension} - to nie był plik Excela"
    try:
        df = pd.read_excel(file_name)
        return (True, df)  # zwracamy 2 wartości - Tupla
    except Exception as e:
        # print(f"Error read_xlsx -> {e}")
        # np. próba otwarcia pliku innego niż xlsx
        # Error read_xlsx -> Excel file format cannot be determined, you must specify an engine manually.
        return (False, f"Error - {e}")


def write_df_to_xlsx(df_to_write, file_name):
    """read DataFrame, write Excel"""
    try:
        df_to_write.to_excel(file_name, engine="openpyxl")
        return True
    except:
        return False

def split_to_xlsx(df, selected_owner, path, column_name="Owner Org"):
    """split our df to many dfs"""
    unique_owners = df[column_name].unique()
    # zamiana NDArray na listę zwykłą: metoda tolist()
    unique_owners = unique_owners.tolist()
    info = None
    for owner in unique_owners:
        df_owner = owner.replace(" ", "_")
        xlsx_file_name = f"{df_owner}.xlsx"
        df_temporary = df.loc[df[column_name] == owner]
        write_df_to_xlsx(df_temporary, path + xlsx_file_name)
        if owner == selected_owner:
            info = "Ważne informacje"

    return info
