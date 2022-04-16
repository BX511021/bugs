import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umeitu.com/bizhitupian/weimeibizhi/"
resp= requests.get(url)
resp.encoding="utf-8"
#print(resp.text)

main_page=BeautifulSoup(resp.text, "html.parser")
resp.close()

#print(main_page)

alist=main_page.find("div",class_="TypeList").find_all("a")
for a in alist:
    href=a.get("href")
    href="https://www.umeitu.com"+href

    child_page_resp=requests.get(href)
    child_page_resp.encoding="utf-8"
    child_page_text=child_page_resp.text
    child_page=BeautifulSoup(child_page_text,"html.parser")

    p=child_page.find("p",align="center")
    img=p.find("img")
    src=img.get("src")

    img_resp=requests.get(src)

    img_name=child_page.find("title")
   #print(img_name.text)
    name_it=img_name.text.split(" ")[0]
    f=open("img/"+name_it+".jpg", mode="wb")
    f.write(img_resp.content)
    f.close()
    child_page_resp.close()
    img_resp.close()
    print("overit!!",name_it)
    time.sleep(2)


print("ALLover!!")