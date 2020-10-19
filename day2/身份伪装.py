from urllib import request
url = "http://www.httpbin.org/headers"
# res = request.urlopen(url).read().decode()
# print(res)
headers = {
    'user-agent':'wenguang',
    'referer':'http://www.xbiquge.la/15/15409/'
}
# 构建一个request对象
req = request.Request(url,headers=headers)
res = request.urlopen(req).read().decode()
print(res)
#referer
