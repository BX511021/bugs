import re
import requests
from concurrent.futures import ThreadPoolExecutor
import csv
counter=1

def fn(num):
    # print(num)
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
        url1 = i.group("url")
        child_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
        child_resp = requests.get(url1, headers=child_headers)
        child_resp_content = child_resp.text
        # 搜索页面内容
        obj2 = re.compile(' <span property="v:summary.*?>(?P<filecontent>.*?)</span>', re.S)
        child_page_content = obj2.search(child_resp_content)
        # 写入新文件

        # print(child_page_content.group("filecontent").replace("<br />",'').replace(" ",'').strip())
        f = open("简介们/" + i.group("name") + '.txt', mode="a", encoding="utf-8")
        f.write(child_page_content.group("filecontent").replace("<br />", '').replace(" ", '').strip())
        f.close()
        child_resp.close()
        print("over!", i.group("name"),counter)
        counter=counter+1


#获取链接
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as T:
        for num in range(0,250,25):
            T.submit(fn,num=num)



    print("ALLover!")

print("Great")

