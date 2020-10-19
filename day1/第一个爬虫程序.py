from urllib import request
from urllib import parse
import re
# url:字符串格式
# get请求
# response = request.urlopen('http://www.baidu.com')
# # print(response)
# result = response.read() # 响应的二进制流
# # decode() 解码  encode() 编码
# s1 = result.decode('utf-8')  #解码后的内容
# print(s1)
# with open("baidu.html",'w',encoding='utf-8') as w:
#     w.write(s1)

# result = request.urlopen('http://www.baidu.com').read().decode('utf-8')
# print(result)
# with open("baidu.html",'w',encoding='utf-8') as w:
#     w.write(result)


# 发送post请求
# url = "https://www.iqianyue.com/mypost"
# #请求体
# data = {
# 'name': 'pythonniubi',
# 'pass': '888888',
# }
# data = bytes(parse.urlencode(data),encoding='utf-8')
# print(data)
# data = parse.urlencode(data).encode('utf-8')
# print(data)
# result = request.urlopen(url,data=data).read().decode('utf-8')
# print(result)
# result = request.urlopen(url,data=b'name=wenguang&pass=heheda').read().decode('utf-8')
# print(result)


# 压缩流的处理
import gzip
url = "http://www.xbiquge.la/xiaoshuodaquan/"
res = request.urlopen(url).read()
try:
    res = gzip.decompress(res).decode('utf-8')
except:
    res = res.decode('utf-8')
rule = '<a href=".*">(.*?)</a></li>' # 正则规则
book_names = re.findall(rule,res) # 开始匹配
print(book_names)

