


class TestParser(unittest.TestCase):

        def test_limit(self):
                feed = "https://www.onliner.by/feed"
                wrong_feed = "https://www.onliner.by"
                not_work_url = "https://www.onliwecdsner.by/"

                parser_1 = Parser(feed)
                parser_2 = Parser(wrong_feed)
                parser_3 = Parser(not_work_url)





