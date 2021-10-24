import json
from datetime import datetime
from email.utils import parsedate_to_datetime
from html import unescape
import re
from logger import logger

time_stamps = ("%b %d %Y at %I:%M%p",
               "%B %d, %Y, %H:%M:%S",
               "%a,%d/%m/%y,%I:%M%p",
               "%a, %d %B, %Y",
               "%Y-%m-%dT%H:%M:%SZ",
               )


@logger
def formatter(text, colorize=False):
    """

    :param text:
    :param colorize:
    :return:
    """
    text = json.loads(text)
    if colorize:
        color = "\033[91m"
    else:
        color = "\033[0m"
    color_end = "\033[0m"

    if text:
        header = f"{color}{text.get('info')}{color_end}\n"
        content = "".join([f"\n{color}Title{color_end}: {article.get('title')}\n"
                           f"{color}Pubdate{color_end}: {article.get('pubDate')}\n"
                           f"{color}Description{color_end}: {article.get('description')}\n"
                           f"{color}Link{color_end}: {article.get('link')}\n"f""
                           f"{color}Media{color_end}: {article.get('media')}\n"
                           for article in text.get("content")]
                          )
        return header + content


def get_datetime(date):
    """Converts date sting to python datetime format
    :param date : str
    :return: datetime
    """
    try:
        time = parsedate_to_datetime(date)
    except Exception:
        for ts in time_stamps:
            try:
                time = datetime.strptime(date, ts)
                return time.date()
            except Exception:
                pass
    else:
        return time.date()


def normalize_data(text):
    """
    Removes html code and specific characters from text
    :param text: str
    :return: data: str
    """
    result = unescape(re.sub("<[^<]+?>", '', text.strip()))
    return result


def get_media_ns(data):
    """
    Find url media name space
    :param data: str
    :return: str
    """
    return re.findall(r'xmlns:media="(\S+/)', data)[0]
