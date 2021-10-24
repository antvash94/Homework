import datetime
import json
import unittest
from unittest.mock import patch
from AntonVashkevich.rss_parser.utils import common, rss_parser, db


with open("mock_rss_feed.txt") as file:
    request = file.read()


class MockRequests:
    def __init__(self, url, limit=None):
        self._r = request
        self.text = request


def mock_requests_get(url):
    return MockRequests(url)


class TestParser(unittest.TestCase):

    @patch("rss_parser.requests.get", side_effect=mock_requests_get)
    def test_parser(self, *args):
        feed = rss_parser.Parser("http://example.com/", 1)
        mock_r = {'title': 'Lorem ipsum 2021-10-23T12:17:00Z',
                  'description': 'Proident velit enim nisi nulla ex ipsum fugiat nostrud.',
                  'link': 'http://example.com/test/1634991420',
                  'pubDate': 'Sat, 23 Oct 2021 12:17:00 GMT'
                  }
        mock_json = {"info": "http://example.com/",
                     "content": [{"title": "Lorem ipsum 2021-10-23T12:17:00Z",
                                  "description": "Proident velit enim nisi nulla ex ipsum fugiat nostrud.",
                                  "link": "http://example.com/test/1634991420",
                                  "pubDate": "Sat, 23 Oct 2021 12:17:00 GMT"}]
                     }
        self.assertEqual(len(feed.get_articles()), 1)
        self.assertEqual(feed.url, "http://example.com/")
        self.assertDictEqual(feed.get_articles()[0], mock_r)
        self.assertTrue(json.loads(feed.to_json()))
        self.assertEqual(feed.to_json(), json.dumps(mock_json))

    @patch("rss_parser.requests.get", side_effect=mock_requests_get)
    def test_output(self, *args):
        feed = rss_parser.Parser("http://example.com/", 2)
        print(common.formatter(feed.to_json()))
        print(common.formatter(feed.to_json(), colorize=True))


class TestUtils(unittest.TestCase):

    def test_get_ns(self):

        self.assertEqual(common.get_media_ns(request), "http://search.yahoo.com/mrss/")

    def test_normalize(self):
        s = "<a><p>&#39hello&#39</a></p>"
        self.assertEqual(common.normalize_data(s), "'hello'")

    def test_date(self):
        date = ["2021-10-23T05:44:33Z", "Sat, 23 Oct 2021 10:10:32 +0300", "Sat, 23 Oct 2021 15:39:00 GMT"]
        for i in date:
            self.assertEqual(common.get_datetime(i), datetime.datetime.strptime('23102021', "%d%m%Y").date())


class TestDB(unittest.TestCase):
    def test_db(self):
        item_1 = {"info": "http://example.com/",
                  "content": [{"title": "Lorem ipsum 2021-10-23T12:17:00Z",
                               "description": "Proident velit enim nisi nulla ex ipsum fugiat nostrud.",
                               "link": "http://example.com/test/1634991420",
                               "pubDate": "Sat, 23 Oct 2021 12:17:00 GMT"}]
                     }

        item_2 = {"info": "http://example.com/",
                  "content": [{"title": "Lorem ipsum 2021-10-23T12:17:00Z",
                               "description": "Proident velit enim nisi nulla ex ipsum fugiat nostrud.",
                               "link": "http://example.com/test/1634991420",
                               "pubDate": "Sat, 23 Oct 2021 12:17:00 GMT"},
                              {"title": "Lorem ipsum 2021-10-23T12:16:00Z",
                               "description": "Non consequat ea incididunt reprehenderit esse exercitation et.",
                               "link": "http://example.com/test/1634991360",
                               "pubDate": "Sat, 23 Oct 2021 12:16:00 GMT"}
                              ]
                     }
        item_3 = {'info': 'News archive\nDate:2021-10-23\nFeed:http://example.com/\n',
                  'content': [{'title': 'Lorem ipsum 2021-10-23T12:17:00Z',
                               'pubDate': '2021-10-23',
                               'description': 'Proident velit enim nisi nulla ex ipsum fugiat nostrud.',
                               'link': 'http://example.com/test/1634991420', 'media': None},
                              {'title': 'Lorem ipsum 2021-10-23T12:16:00Z',
                               'pubDate': '2021-10-23',
                               'description': 'Non consequat ea incididunt reprehenderit esse exercitation et.',
                               'link': 'http://example.com/test/1634991360',
                               'media': None}]}

        for i in (item_1, item_2):
            db.insert_data(json.dumps(i))

        query_1 = db.get_json_from_db("20211023")
        query_2 = db.get_json_from_db("20211023", "http://example.com/")
        self.assertEqual(len(json.loads(query_1)["content"]), 2)
        self.assertDictEqual(json.loads(query_2), item_3)


if __name__ == '__main__':
    unittest.main()