import requests

session=requests.session()

url="https://passport.17k.com/ck/user/login"
data={
    "loginName":"bxbz",
    "password":"Libojia0408"
}

resp1=session.post(url,data=data)
#print(resp.text)
resp2=session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp2.json())