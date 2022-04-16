import requests

url = 'http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=88093251_83_hao_pg&wd=%E5%90%8A%E5%B8%A6%E8%A2%9C%E5%A4%A9%E4%BD%BF&fenlei=256&oq=request%25E5%258C%2585%25E6%2597%25A0%25E6%25B3%2595%25E6%258A%2593%25E5%258F%2596%25E7%25BD%2591%25E9%25A1%25B5%25E6%25BA%2590%25E7%25A0%2581%25E4%25B9%25B1%25E7%25A0%2581&rsv_pq=859da531000ffd34&rsv_t=fcd2xyZ9GxmLNktubklrd%2BL%2BMBpY0Gu2516OpoPLrYS4xgAODojsG6l21Dbuc6%2FkzldH8rjw1Kho&rqlang=cn&rsv_enter=1&rsv_dl=th_3&rsv_btype=t&inputT=1527&rsv_sug3=46&rsv_sug1=31&rsv_sug7=001&rsv_sug2=1&rsp=3&rsv_sug9=es_0_1&rsv_sug4=1527&rsv_sug=9'


#headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
resp = requests.get(url)
resp.encoding='utf-8'
print(resp)
print(resp.text)
f = open("canwe.html", 'w', encoding='utf-8')
f.write(resp.text)
f.close()
resp.close()