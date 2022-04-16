# coding:utf-8
import requests
import json
from bs4 import BeautifulSoup

# 搜索页面
def get_home_page(page):
    html = "https://s.weibo.com/article?q=%E5%8F%B0%E9%A3%8E%E5%B1%B1%E7%AB%B9&Refer=weibo_article&page={}".format(page)
    respone = requests.get(html)
    # print(respone.text)
    textHtml = respone.text
    soup = BeautifulSoup(textHtml,features="lxml")
    info_all = soup.select(".card-wrap div div h3 a")
    a_list = []
    for item in info_all:
        a_href = item['href']
        a_list.append(a_href)

    return a_list

# 爬起文章页面
def get_content(html_1):
    # html_1 = "https://weibo.com/ttarticle/p/show?id=2309404344349319115732" # 测试用的
    header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "Cookie":"SINAGLOBAL=3045531231804.757.1542339154287; UOR=,,www.baidu.com; wb_view_log=1536*8641.25; un=18722846347; wvr=6; wb_view_log_5816188628=1536*8641.25; wb_timefeed_5816188628=1; Ugrow-G0=169004153682ef91866609488943c77f; ALF=1582963311; SSOLoginState=1551427312; SCF=AqVoDry8DgrNPZLa7pkwesp4oyNNCWdcpgWQj1ZQ-7Z-GLuL8HEFsKKTy9LKsa0aIgLjeETtnBpvLqf1pFX-H9o.; SUB=_2A25xfJagDeRhGeNG6lQQ-CbKyTSIHXVSC49orDV8PUNbmtBeLXmmkW9NS2iTzhh_-emgxKLZvYfKTt4TWxAYQ4t0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_VVQdF_QKBI9FlsOrs.5c5JpX5KzhUgL.Fo-ReKqp1hnceon2dJLoIXzLxKnLB--LBo5LxK-LB.qL1hqLxKML1-2L1hBLxK-L1-zLBoBLxKnL1hBL1KqLxK-LBo5L12qLxKMLB-2L1-BR1h-t; SUHB=0A0JvAxWF_4iQM; YF-V5-G0=3717816620d23c89a2402129ebf80935; _s_tentry=login.sina.com.cn; Apache=8257276420249.566.1551427311659; YF-Page-G0=d52660735d1ea4ed313e0beb68c05fc5; ULV=1551427311697:7:2:3:8257276420249.566.1551427311659:1551408473325; webim_unReadCount=%7B%22time%22%3A1551427323547%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A41%2C%22msgbox%22%3A0%7D; WBStorage=f3685954b8436f62|undefined",
        "Host":"weibo.com",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }
    get_text = requests.get(html_1,headers=header)
    # print(get_text.text)
    soup_text = BeautifulSoup(get_text.text,features="lxml")
    article_title = soup_text.select("div.title")[0].text
    article_content = soup_text.select("div.WB_editor_iframe")[0].text
    print("获取成功")
    return {"article_title":article_title,"article_content":article_content}

def run():
    # 获取五十页的关键字文章
    n = 100
    article_content = []
    for i in range(1,n):
        a_list = get_home_page(i)
        for url in a_list:
            try:
                article = get_content(url)
                article_content.append(article)
            except:
                print("内容有问题")
    with open("./article_file/all_article.json","w",encoding="gbk") as f:
        json.dump(article_content,f)

if __name__=="__main__":
    run()