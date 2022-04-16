import requests
from bs4 import BeautifulSoup

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
resp=requests.post(url)

print(resp)

f = "00e0b509f6259df8642dbc35" \
    "662901477df22677ec152b5ff6" \
    "8ace615bb7b725152b3ab17a87" \
    "6aea8a5aa76d2e417629ec4ee341f" \
    "56135fccf695280104e0312ecbda92557" \
    "c93870114af6c9d05c4f7f0c3685b7a4" \
    "6bee255932575cce10b424d813cfe487" \
    "5d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

g ="0CoJUm6Qyw8W8jud"
e = "010001"
data={
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_31649694",
    "threadId": "R_SO_4_31649694"
}


"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d:数据  e:固定数值010001 f：很长的固定值，g:固定值
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""