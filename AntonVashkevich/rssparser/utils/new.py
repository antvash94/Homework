from jinja2 import Template
from AntonVashkevich.rssparser.utils.rss_parser import Parser
import json


def convert_to_html(data):

    """"""
    data_json = json.loads(data)
    info = data_json.get("info").get("title")
    content = data_json.get("content")
    with open("../templates/base.html") as file:
        new_file = file.read()
        template = Template(new_file)
        with open(f"{info}.html", "w") as f:
            f.write(template.render(info=info, content=content))


convert_to_html(Parser("https://www.onliner.by/feed").to_json())

