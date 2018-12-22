import re
import requests
from html import unescape


def http_or_https(s):
    return s.startswith("http") or s.startswith("https")


if __name__ == '__main__':
    r = requests.get("https://book.douban.com/subject/26967597/")
    results = re.findall('.*?href="(.*?)"', r.text, re.S)
    for h in filter(http_or_https, results):
        print(unescape(h))
