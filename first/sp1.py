import requests as requests
from bs4 import BeautifulSoup
import lxml


def get_html():
    url = "https://www.sanwen.net/"
    two_html = ['sanwen', 'shige', 'zawen', 'suibi', 'rizhi', 'novel']
    for doc in two_html:

        if doc == 'sanwen':
            print("running sanwen -----------------------------")
        if doc == 'shige':
            print("running shige ------------------------------")
        if doc == 'zawen':
            print('running zawen -------------------------------')
        if doc == 'suibi':
            print('running suibi -------------------------------')
        if doc == 'rizhi':
            print('running ruzhi -------------------------------')
        if doc == 'nove':
            print('running xiaoxiaoshuo -------------------------')
    i = 1
    while (i < 10):
        par = {'p': i}
        res = requests.get(url + doc + '/', params=par)
    if res.status_code == 200:
        soup(res.text)
        i += i
