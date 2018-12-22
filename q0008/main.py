import requests
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get("https://book.douban.com/subject/26967597/")
    content = re.sub(r'<script.*?>.*?</script>|<style.*?>.*?</style>', '', r.text, flags=re.S)
    soup = BeautifulSoup(content, 'lxml')
    print(soup.get_text().replace('\n\n\n', ''))
