import requests
from bs4 import BeautifulSoup
url="https://www.pearvideo.com/video_1752547"
resp1=requests.get(url)
resp1.encoding="utf-8"
main_page=BeautifulSoup(resp1.text, "html.parser")
resp1.close()
name=main_page.find("title")
print(name.text)



contid=url.split("_")[-1]
videosatutsURL = f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.19270561968745592"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Referer": url
}
# print(contid)
resp=requests.get(videosatutsURL,headers=headers)
systime=resp.json()["systemTime"]
srcUrl=resp.json()["videoInfo"]["videos"]["srcUrl"]
#https://video.pearvideo.com/mp4/adshort/20220222/cont-1752547-15830346_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20220222/1645579238780-15830346_adpkg-ad_hd.mp4

srcUrl=srcUrl.replace(systime,"cont-"+contid)
f=open(name.text+".mp4",mode="wb")
f.write(requests.get(srcUrl).content)
f.close()
resp.close()
print("over11")