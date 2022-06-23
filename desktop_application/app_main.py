from functions_df.xlsx_operations import *
import PySimpleGUI as sg
import sys

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
            readed, df = read_from_xlsx(values["Browse"])
            if readed:
                # mamy df, dzielimy na elementy i zapisujemy do plików
                wynik = split_to_xlsx(df, values[1])
                sg.popup_auto_close(f"Wynik: {wynik}", auto_close_duration=2)
            else:
                print("ERROR!!!")
        else:
            sg.popup_auto_close("Brak file name", auto_close_duration=3)
