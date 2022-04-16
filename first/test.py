from urllib.request import urlopen

html = urlopen("http://www.baidu.com/")
content = html.read().decode('utf-8')
print((content))
f = open('tieba.html', 'w', encoding='utf-8')
f.write(content)
#f.close()