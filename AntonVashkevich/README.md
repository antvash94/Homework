# Final task


# Pure Python command-line RSS reader.
```
positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --date         Print news by date `%Y%m%d` format
  --to_html      Conversion of news in html format
  --to_pdf       Conversion of news in pdf format
  --colorize     Colorize stdout
  --limit LIMIT  Limit news topics if this parameter provided
```
# JSON schema
```
{ "info"  : title,
  "content":
           [ {  "title": title,
                "description": description,
                "link": link,
                "media": media,
                "pubDate": pubdate,
                },
                ...
                ]
                }
```
# Tests
```
 python -m unittest tests.py    
```