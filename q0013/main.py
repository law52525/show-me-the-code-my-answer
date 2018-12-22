from gevent import monkey;monkey.patch_all()  # 一定要置顶
import time
import requests
import re
import os
import gevent.pool

image_path = 'image'
if not os.path.exists(image_path):
    os.mkdir(image_path)


def run_spider(url):
    name = url.split('/')[-1]
    with open(image_path + os.sep + name, 'wb') as f:
        f.write(requests.get(url).content)


def main():
    start = time.time()
    r = requests.get("http://tieba.baidu.com/p/5400710584")
    results = re.findall('<img class="BDE_Image".*?src="(.*?)"', r.text, re.S)

    pool = gevent.pool.Pool(20)
    threads = []
    for result in results:
        threads.append(pool.spawn(run_spider, result))
    gevent.joinall(threads)
    print(time.time() - start)


if __name__ == '__main__':
    main()
