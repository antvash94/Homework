import argparse
import logging
import sys
from utils.rss_parser import Parser
from utils.db import insert_data, get_articles_by_date,get_json
from utils.converter import convert_to_pdf, convert_to_html


__VERSION__ = 1.0
formatter = "%(levelname)s %(asctime)s %(message)s"


def main():
    parser = argparse.ArgumentParser(description="RSS parser")
    parser.add_argument("url", help="input feed url", nargs="?",)
    parser.add_argument("-v", "--version", action="store_true", help="Current version")
    parser.add_argument("--json", action="store_true", help="json stdout")
    parser.add_argument("-l", "--limit", default=None, type=int, help="limit of news")
    parser.add_argument("--verbose", action="store_true", )
    parser.add_argument("--date", type=str, help="get news by date")
    parser.add_argument("--to-html", action="store_true", help='convert to html')
    parser.add_argument("--to-pdf", action="store_true", help='convert to pdf')

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(stream=sys.stderr, format=formatter, level=logging.INFO)
    else:
        logging.basicConfig(filename='log_file.log', format=formatter, level=logging.INFO)

    if args.url:
        rss = Parser(args.url, args.limit)
        insert_data(rss.to_json())

        if args.json:
            sys.stdout.write(str(rss.to_json()))
        elif args.date:
            sys.stdout.write(get_articles_by_date(args.date, rss.link, args.limit))
        else:
            sys.stdout.write(str(rss.make_articles()))
    elif args.to_html:
        convert_to_html(get_json(args.date))
    elif args.to_pdf:
        convert_to_pdf(get_json(args.date))

    elif args.version:
        sys.stdout.write(f"Version:---{__VERSION__}---")

    elif args.date:
        sys.stdout.write(get_articles_by_date(args.date, args.limit))
    else:
        sys.stdout.write("input '-h, --help' for help")


if __name__ == '__main__':
    main()