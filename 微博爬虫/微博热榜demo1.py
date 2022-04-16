# https://weibo.com/ajax/statuses/hot_band
import requests
import re

resp=requests.get("https://weibo.com/ajax/statuses/hot_band")
page_content=resp.text

obj0=re.compile(r''
                r'note":"(?P<note>.*?)".*?rank":(?P<rank>.*?),'
                r'.*?text".*?//(?P<url>.*?)"',re.S)
child_heads={
        "cookie": "SINAGLOBAL=994940441310.3768.1646046432448; SUB=_2AkMVeBXHf8NxqwJRmP8cym_lbYxzwg7EieKjJOQcJRMxHRl-yT9jqnMItRB6Pvg7KA8x7wqVMhgadgKJc2DBeNQ_Y31E; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW9uKDJGdfbiZhGN8a6k.ee; _s_tentry=weibo.com; Apache=3342405387255.0654.1647152154596; ULV=1647152154602:5:4:1:3342405387255.0654.1647152154596:1646228537664",
        "referer": "https://s.weibo.com/weibo?q=%23%E5%90%89%E6%9E%97%E6%96%B0%E5%A2%9E%E6%9C%AC%E5%9C%9F%E7%A1%AE%E8%AF%8A1412%E4%BE%8B%23",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

}



result=obj0.finditer(page_content)

for it in result:
    print(it.group("rank"), end="  ")
    print(it.group("note"))
    child_resp=requests.get("https://"+it.group("url").strip("\\"),headers=child_heads)
    print(child_resp.text)
    child_resp.close()
    break



# print(page_content)

resp.close()