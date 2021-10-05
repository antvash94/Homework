from .rss_parser import Parser
import argparse
import sys
import logging


__VERSION__ = 1.0
formatter = "%(levelname)s %(asctime)s %(message)s"


def main():
    parser = argparse.ArgumentParser(description="RSS parser")
    parser.add_argument("url", help="input feed url", nargs="?",)
    parser.add_argument("-v", "--version", action="store_true", help="Current version")
    parser.add_argument("--json", action="store_true", help="json stdout")
    parser.add_argument("-l", "--limit", default=None, type=int, help="limit of news")
    parser.add_argument("--verbose", action="store_true", )

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(stream=sys.stderr, format=formatter, level=logging.INFO)
    else:
        logging.basicConfig(filename='log_file.log', format=formatter, level=logging.INFO)
    if args.url:
        rss = Parser(args.url, args.limit)
        if args.json:
            sys.stdout.write(str(rss.to_json()))
        else:
            sys.stdout.write(str(rss.make_articles()))
    elif args.version:
        sys.stdout.write(f"Version:---{__VERSION__}---")

    else:
        sys.stdout.write(f"input 'python setup.py -h' for help")


if __name__ == '__main__':
    main()
