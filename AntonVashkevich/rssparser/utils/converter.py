import os
from jinja2 import Template
import json
from fpdf import FPDF
import datetime
from common import download_img
from logger import logger
import glob


@logger
def convert_to_html(data):

    """"""
    data_json = json.loads(data)
    info = data_json.get("info")
    content = data_json.get("content")
    with open("templates/base.html") as file:
        new_file = file.read()
        template = Template(new_file)
        with open(f"{info}{datetime.date.today()}.html", "w") as f:
            f.write(template.render(info=info, content=content))

@logger
def convert_to_pdf(data):
    data_json = json.loads(data)
    info = data_json.get("info")
    content = data_json.get("content")
    pdf = FPDF()

    pdf.alias_nb_pages()
    pdf.add_font('DejaVu', '', 'templates/fonts/DejaVuSansCondensed.ttf', uni=True)

    for i in content:
        pdf.add_page()
        pdf.set_font('DejaVu', '', 16)
        pdf.multi_cell(0, 10, i.get("title"), 0, 1)
        pdf.set_font('DejaVu', '', 12)
        pdf.cell(0, 10, str(i.get("pubDate")), 0, 1)
        if i.get("media"):
            pdf.image(download_img(i.get("media")), w=100)
        if i.get("description"):
            pdf.multi_cell(0, 10, str(i.get("description")), 0, 1)
        pdf.set_font('DejaVu', 'U', 10)
        pdf.cell(0, 10, str(i.get("link")), 0, 1)
        pdf.ln()
    files = glob.glob('templates/image/*')
    for f in files:
        os.remove(f)

    pdf.output(f"{info}:{datetime.date.today()}.pdf")
