from functions_df.xlsx_operations import *
import PySimpleGUI as sg
import sys
import os

# https://pysimplegui.readthedocs.io/en/latest/

interface = [
    [sg.Text("Read from XLSX file:")],
    [sg.Input(), sg.FileBrowse()],
    [sg.Text("Podaj wyróżnionego Ownera:")],
    [sg.Input()],
    [sg.OK(), sg.Button("DoIt")],
]
window = sg.Window("XLSX operations.", interface)
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()

    # sprawdzamy, czy przycisk zawiera się w naszych możliwościach
    if event in ("OK", "Exit"):
        print("Bye bye")
        sys.exit(0)

    if event == "DoIt":
        # sg.popup("Nasze wartości", values)
        if values["Browse"]:
            # /home/adasiek/PycharmProjects/podstawy_python_2022_06/pandas_df/db_test.xlsx
            readed, df = read_from_xlsx(values["Browse"])
            path, file = os.path.split(values["Browse"])
            selected_owner = values[1]  # drugie pole INPUT w interfejsie
            if readed:
                # mamy df, dzielimy na elementy i zapisujemy do plików
                wynik = split_to_xlsx(df, selected_owner, path + "/")
                sg.popup_auto_close(f"Wynik: {wynik}", auto_close_duration=2)
            else:
                print(f"Komunikat z funkcji read -> {df} ")
        else:
            sg.popup_auto_close("Brak file name", auto_close_duration=3)
