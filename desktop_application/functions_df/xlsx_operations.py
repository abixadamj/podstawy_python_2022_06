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
