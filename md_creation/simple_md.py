"""
Prosty skrypt generujący plik w formacie Markdown
https://www.markdownguide.org/basic-syntax/
"""

import snakemd

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

doc.output_page()
