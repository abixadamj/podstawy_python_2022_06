"""
Prosty skrypt generujący plik w formacie Markdown
https://www.markdownguide.org/basic-syntax/
"""

import subprocess  # wywoływanie poleceń systemowych !!!
import snakemd
from snakemd import Paragraph, InlineText
import pandas as pd


df = pd.read_csv("dane_sprzedazowe.csv", sep=";")
print(df)

doc = snakemd.new_doc("simple_md_file")

doc.add_header("To będzie tytuł", 3)
doc.add_paragraph("Dzisiaj tworzymy dokument w MD")
doc.add_horizontal_rule()
my_par = """
To jest długi tekst,
może mieć wiele linijek....

I jest identyczny z tym, co piszemy ;-)
"""
doc.add_paragraph(my_par)
doc.add_horizontal_rule()

# dodatnie paragrafu z tekstem Italic/Pochyłym
doc.add_element(
    Paragraph(
        [InlineText("Test DataFrame", italics=True)]
    ))
# tworzymy listę list z wartości data frame
data_sales = df.values.tolist()
print(data_sales)
table_header = ["**Rok**", "~~Sprzedaż kart 5GB~~", "*Sprzedaż Abonamentów*", "Światłowody"]
# tworzymy tabelę z nagłówkiem i danymi
doc.add_table(
    table_header,
    data_sales, )

doc.output_page()

# dodamy wywołanie pandoc'a
# https://docs.python.org/3/library/subprocess.html#module-subprocess

# pandoc -o dokument.docx simple_md_file.md
ret_code = None
try:
    command = ["pandoc", "-o", "dokument.xlsx", "simple_md_file.md"]
    ret_code = subprocess.run(command, capture_output=True)
    print(f"Returned: {ret_code}")
except:
    print(f"ERROR: {ret_code}")
