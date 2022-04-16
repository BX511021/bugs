import requests
from bs4 import BeautifulSoup
url="https://movie.douban.com/top250"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
resp = requests.get(url,headers=headers)
#print(resp)

page = BeautifulSoup(resp.text,"html.parser")
#table=page.find("ol", class_="grid_view")
table = page.find("ol", attrs={"class": "grid_view"})

#print(table)

name=table.find_all("span", class_="title")
for it in name:
    chan=it.text.strip()
    print(chan)