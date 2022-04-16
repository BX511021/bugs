import requests

url ="https://fanyi.baidu.com/sug"

s = input("请输入搜寻目标")

dat = {
    "kw" : s
}
resp = requests.post(url, data=dat)
print(resp.json())