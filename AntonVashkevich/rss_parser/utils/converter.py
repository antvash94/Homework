import os
from jinja2 import Template
import json
from fpdf import FPDF
import datetime
import requests
from urllib.parse import urlparse
from logger import logger
import glob


path_to_html = os.path.join(os.path.dirname(__file__), 'templates', 'base.html')


def download_img(image_path, image_url):
    """
    Download image to template dir and return path to file
    :param image_url: str
    :param image_path:str
    :return: str
    """
    img_data = requests.get(image_url).content
    img_path = os.path.join(image_path, str(hash(image_url))+".jpg")
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    return img_path


@logger
def convert_to_html(data):

    """
    Convert parsed JSON data to html format.

    :param data: json:
    :return None
    """
    data_json = json.loads(data)
    info = data_json.get("info")
    content = data_json.get("content")
    with open(path_to_html) as file:
        new_file = file.read()
        template = Template(new_file)
        with open(f"{urlparse(info).netloc} {datetime.date.today()}.html", "w") as f:
            f.write(template.render(info=info, content=content))


@logger
def convert_to_pdf(data):
    """
    Convert parsed JSON data to pdf format.

    :param data: json:
    :return None
    """
    pdf = FPDF()
    path_to_pdf = os.path.join(os.path.dirname(__file__),  'templates/fonts', 'DejaVuSansCondensed.ttf')
    path_to_image = os.path.join(os.path.dirname(__file__),  'image')
    data_json = json.loads(data)
    info = data_json.get("info")
    content = data_json.get("content")

    pdf.alias_nb_pages()
    pdf.add_font('DejaVu', '', path_to_pdf, uni=True)

    for i in content:
        pdf.add_page()
        pdf.set_font('DejaVu', '', 16)
        pdf.multi_cell(0, 10, i.get("title"), 0, 1)
        pdf.set_font('DejaVu', '', 12)
        pdf.cell(0, 10, str(i.get("pubDate")), 0, 1)
        if i.get("media"):
            pdf.image(download_img(path_to_image, i.get("media")), w=100)
        if i.get("description"):
            pdf.multi_cell(0, 10, str(i.get("description")), 0, 1)
        pdf.set_font('DejaVu', 'U', 10)
        pdf.cell(0, 10, str(i.get("link")), 0, 1)
        pdf.ln()
    files = glob.glob(os.path.join(path_to_image + "/*jpg"))
    for f in files:
        os.remove(f)
    pdf.output(f"{urlparse(info).netloc}:{datetime.date.today()}.pdf")
