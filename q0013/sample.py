import requests
import re


r = requests.get("http://tieba.baidu.com/p/5400710584")
result = re.search('<div.*?&quot;post_no&quot;:29.*?<img class="BDE_Image".*?src="(.*?)"', r.text, re.S)
if result:
    with open('cat.jpg', 'wb') as f:
        f.write(requests.get(result.group(1)).content)
