import requests
import xml.etree.ElementTree as et
import json
import logging
from exceptions import NotXml
from logger import logger
import os
from common import normalize_data, get_media_ns


class Parser:
    def __init__(self, url, limit=None):
        logging.warning(f"create {url} parser")
        self.url = url
        self.limit = limit
        try:
            self._r = requests.get(self.url)
            try:
                root = et.fromstring(self._r.text)

            except et.ParseError:
                logging.error(NotXml)
            else:
                self.root = root
                parent = str([i.tag for i in self.root][0])
                child = "item" if parent == "channel" else "entry"
                self._path = os.path.join(".", parent, child)
                self.link = self.root.find(os.path.join(".", parent, "link")).text

        except Exception as ex:
            logging.error(ex)

    @logger
    def get_channel_info(self):
        channel = self.root.find(".")
        info = {i.tag: i.text for i in channel[0]}
        return info

    @logger
    def get_articles(self):
        items = self.root.findall(f"{self._path}")
        media_tags = ["{" + get_media_ns(self._r.text) + "}content",
                      "{" + get_media_ns(self._r.text) + "}thumbnail",
                      "enclosure"
                      ]
        articles = []
        for item in items:
            temp = {}
            for tag in item:
                if not tag.text:
                    if tag.tag in media_tags:
                        temp["media"] = tag.attrib.get("url")
                    else:
                        temp[tag.tag] = tag.attrib
                else:
                    temp[tag.tag] = normalize_data(tag.text)
            articles.append(temp)
        if self.limit:
            return articles[:self.limit]
        return articles

    @logger
    def make_articles(self):
        headers = self.get_channel_info()
        articles = self.get_articles()

        if headers and articles:
            header = f"{headers.get('title')}\n{headers.get('description')}\n{headers.get('link')}\n"
            content = "".join([f"\nTitle: {article.get('title')}\n"
                               f"Pubdate: {article.get('pubDate')}\n"
                               f"Description: {article.get('description')}\n"
                               f"Link: {article.get('link')}\n"f""
                               f"Media: {article.get('media')}\n"
                               for article in articles]
                              )
            return header + content

    @logger
    def to_json(self):
        file = {"info": self.get_channel_info(),
                "content": self.get_articles()
                }
        return json.dumps(file, ensure_ascii=False)

    def __repr__(self):
        return f"{self.make_articles()}"
