import requests
import re
import csv
domian="https://dytt89.com/"

resp=requests.get(domian)
resp.encoding='gb2312'


obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S )
obj2 = re.compile(r'''<li><a href='(?P<nurl>.*?)' title=".*?">''', re.S)
obj3 = re.compile(r'◎译　　名　(?P<Ename>.*?)<br />'
                  r'◎片　　名　(?P<name>.*?)<br />◎年　　代　(?P<year>.*?)<br />'
                  r'◎产　　地　(?P<land>.*?)<br />◎类　　别　(?P<type>.*?)<br />'
                  r'◎语　　言　(?P<langeuage>.*?)<br />◎字　　幕　(?P<word>.*?)<br />'
                  r'◎上映日期　(?P<date>.*?)<br />'
                  r'◎豆瓣评分　(?P<Dscore>.*?) from (?P<Dnum>.*?) users<br />'
                  r'◎IMDb评分　(?P<Iscore>.*?) from (?P<Inum>.*?) users<br />',re.S)
result1 = obj1.finditer(resp.text)
child_list=[]
for it in result1:
    ul=it.group('ul')
    result2 = obj2.finditer(ul)

    for itm in result2:
       # print(itm.group('nurl'))
        child_herf=domian+itm.group('nurl').strip('/')
        child_list.append(child_herf)
       # print(child_herf)

f = open("data2.csv", mode="a", encoding="gb2312")
csvwritter = csv.writer(f)

for href in child_list:
    child_resp=requests.get(href)
    #print(child_resp)
    child_resp.encoding='gb2312'
    s=obj3.search(child_resp.text)
    dic=s.groupdict()
    csvwritter.writerow(dic.values())

f.close()
print('over!!')




