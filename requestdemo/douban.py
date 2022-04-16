import requests

url = "https://movie.douban.com/j/chart/top_list"

param={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
resp=requests.get(url=url, params=param,headers=headers)

print(resp.json())
resp.close()