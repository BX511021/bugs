import re
import requests
import csv

for num in range(0,250,25):
    print(num)
    url = f"https://movie.douban.com/top250?start={num}&filter="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text

    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?'
                     r'<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<range>.*?)</span>.*?'
                     r'<span>(?P<number>.*?)人评价</span>.*?</li>', re.S)

    result = obj.finditer(page_content)
    f = open("data.csv", mode="a", encoding="utf-8")
    csvwritter = csv.writer(f)
    for it in result:
        # print(it.group("year").strip())
        # print(it.group("number"))
        # print(it.group("range"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwritter.writerow(dic.values())
    f.close()
    print("over!!")


