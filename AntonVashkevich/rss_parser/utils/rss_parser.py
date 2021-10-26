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
    parse rss feed
    :return list of item dicts
    to_json()
    :return json
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
            self._r = requests.get(self.url)
            try:
                root = et.fromstring(self._r.text)

            except et.ParseError:
                logging.error(NotXml)
                self.root = None
            else:
                self.root = root
                parent = str([i.tag for i in self.root][0])
                child = "item" if parent == "channel" else "entry"
                self._path = os.path.join(".", parent, child)
                self.link = self.root.find(os.path.join(".", parent, "link")).text

        except Exception as ex:
            logging.error(ex)
            self.root = None
    @logger
    def get_articles(self):
        items = self.root.findall(f"{self._path}")
        media_tags = ["{" + get_media_ns(self._r.text) + "}content",
                      "{" + get_media_ns(self._r.text) + "}thumbnail",
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

