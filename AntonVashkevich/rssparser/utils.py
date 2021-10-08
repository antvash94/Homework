from datetime import datetime
from email.utils import parsedate_to_datetime
from html import unescape
from unicodedata import normalize
import re
time_stamps = ("%b %d %Y at %I:%M%p",
               "%B %d, %Y, %H:%M:%S",
               "%a,%d/%m/%y,%I:%M%p",
               "%a, %d %B, %Y",
               "%Y-%m-%dT%H:%M:%SZ",
               )


def get_datetime(date):
    """"""
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


def normalize_data(data):
    """"""
    try:
        result = unescape(re.sub("<[^<]+?>", '', data.strip()))
        return result
    except Exception:
        return data


def get_media_ns(data):
    """"""
    return re.findall(r'xmlns:media="(\S+/)', data)[0]





