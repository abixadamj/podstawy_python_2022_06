import PySimpleGUI as sg
import sys

# https://pysimplegui.readthedocs.io/en/latest/

interface = [
    [sg.Text("Make sth with XLSX")],
    [sg.Input(), sg.FileBrowse()],
    [sg.Text("Podaj wyróżnionego Ownera:")],
    [sg.Input()],
    [sg.OK(), sg.Button("DoIt")],
]
window = sg.Window("XLSX.", interface)
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()

    # sprawdzamy, czy przycisk zawiera się w naszych możliwościach
    if event in ("OK", "Exit"):
        print("Bye bye")
        sys.exit(0)

    if event == "DoIt":
        sg.popup("Nasze wartości", values)
