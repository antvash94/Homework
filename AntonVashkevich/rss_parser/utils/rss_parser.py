import requests
import xml.etree.ElementTree as et
import json
import logging
from exceptions import NotXml
from logger import logger
import os
from common import normalize_data, get_media_ns


class Parser:
    """
    :methods
    get_articles()
    to_json()
    """
    def __init__(self, url, limit=None):
        """

        :param url: str
        feed url
        :param limit: int
        limit of news
        """
        logging.info(f"create {url} parser")
        self.url = url
        self.limit = limit
        try:
            self._r = requests.get(self.url).text
            try:
                self.xml = et.fromstring(self._r)

            except et.ParseError:
                logging.error(NotXml)
                raise NotXml(f"{self.url} is not rss feed")
            else:
                self.root = self.xml
                parent = str([i.tag for i in self.root][0])
                child = "item" if parent == "channel" else "entry"
                self._path = os.path.join(".", parent, child)
                self.link = self.root.find(os.path.join(".", parent, "link")).text

        except Exception as ex:
            logging.error(ex)

    @logger
    def get_articles(self):
        items = self.root.findall(f"{self._path}")
        media_tags = ["{" + get_media_ns(self._r) + "}content",
                      "{" + get_media_ns(self._r) + "}thumbnail",
                      "enclosure"
                      ]
        target = ["title", "pubDate", "description", "link"]
        articles = []
        for item in items:
            temp = {}
            for tag in item:
                if tag.tag in media_tags:
                    temp["media"] = tag.attrib.get("url")
                elif tag.tag in target:
                    temp[tag.tag] = normalize_data(tag.text)
            articles.append(temp)
        if self.limit:
            return articles[:self.limit]
        return articles

    @logger
    def to_json(self):
        file = {"info": self.link,
                "content": self.get_articles()
                }
        return json.dumps(file, ensure_ascii=False)

    def __repr__(self):
        return f"{self.url} parser"

