import re
from concurrent.futures import ThreadPoolExecutor
import requests
import time
# 获取链接
counter = 1
def fn(num):
    global counter
    or_url = f"https://movie.douban.com/top250?start={num}&filter="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    resp = requests.get(or_url, headers=headers)
    page_content = resp.text
    resp.close()
    obj1 = re.compile('<li>.*?<a href="(?P<url>.*?)">.*?width="100" alt="(?P<name>.*?)".*?</li>', re.S)
    page1 = obj1.finditer(page_content)
    for i in page1:
        print("over!", i.group("name"), counter)
        counter = counter + 1


if __name__ == '__main__':
    t1=time.time()

    for num in range(0, 250, 25):
        fn(num)
    t2=time.time()
    print("Great",t2-t1)
