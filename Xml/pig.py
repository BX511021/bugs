import requests
from xml import etree
from lxml import html
url="https://shenyang.zbj.com/search/f/?kw=saas"
resp=requests.get(url)
# print(resp)
#对网页源代码进行解析
htm = html.etree.HTML(resp.text)

divs=htm.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:
    #// *[ @ id = "utopia_widget_76"] / a[2] / div[2] / div[1] / span[1]
    price=div.xpath(".// *[ @ id = 'utopia_widget_76'] / a[2] / div[2] / div[1] / span[1]/text()")[0].strip("¥")
    title="saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    com_name=div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip("\n")
    # print(com_name)
    print(price)
    #print(title)
