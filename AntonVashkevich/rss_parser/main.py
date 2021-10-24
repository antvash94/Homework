import argparse
import logging
import sys
from utils.rss_parser import Parser
from utils.common import formatter
from utils.db import insert_data, get_json_from_db
from utils.converter import convert_to_pdf, convert_to_html


__VERSION__ = 2.0
log_formatter = "%(levelname)s %(asctime)s %(message)s"


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
    parser.add_argument("--colorize", action="store_true", default=False)

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(stream=sys.stderr, format=log_formatter, level=logging.INFO)
    else:
        logging.basicConfig(filename='log_file.log', format=log_formatter, level=logging.INFO)
    if args.version:
        sys.stdout.write(f"Version:---{__VERSION__}---")

    if args.url and not args.date:
        rss = Parser(args.url, args.limit)
        insert_data(rss.to_json())
        content = rss.to_json()
        if args.json:
            sys.stdout.write(content)
        else:
            sys.stdout.write(formatter(content, colorize=args.colorize))
        if args.to_html:
            convert_to_html(content)

        if args.to_pdf:
            convert_to_pdf(content)

    elif args.url and args.date:
        rss = Parser(args.url, args.limit)
        insert_data(rss.to_json())
        content = get_json_from_db(date=args.date, link=rss.link, limit=args.limit)
        if args.json:
            sys.stdout.write(content)
        else:
            sys.stdout.write(formatter(content, colorize=args.colorize))
        if args.to_html:
            convert_to_html(content)
        if args.to_pdf:
            convert_to_pdf(content)

    elif args.date and not args.url:
        content = get_json_from_db(date=args.date, link=None, limit=args.limit)
        sys.stdout.write(formatter(content))

    else:
        sys.stdout.write(" -h, --help  show this help message and exit")


if __name__ == '__main__':
    main()