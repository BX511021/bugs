import re
lst = re.findall(r"\d+","我的电话是10086，我男朋友的电话时10010")

print((lst))

    #it = re.finditer(r"\d+", "我的电话是10086，我男朋友的电话时10010")

    #for i in it:
     #   print(i.group())
obj=re.compile(r"\d+")

s = obj.search("我的电话是10086，我男朋友的电话时10010")

print(s.group())