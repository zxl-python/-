# 对urllib的封装
import json
import gzip
from urllib import request,parse
from http.cookiejar import CookieJar
from lxml import etree

cookiejar = CookieJar()
# cookiejar处理器
cookiejar_handler = request.HTTPCookieProcessor(cookiejar)
def get(url,params={},headers={},cookies={},proxies={},timeout=None):
    return requests(url=url,method='GET',data=params,headers=headers,cookies=cookies,proxies=proxies,timeout=timeout)

def post(url,data={},headers={},cookies={},proxies={},timeout=None):
    return requests(url=url, method='POST',data=data,headers=headers,cookies=cookies,proxies=proxies,timeout=timeout)

def requests(url,method='GET',data={},headers={},cookies={},proxies={},timeout=None):
    req = request.Request(url,headers=headers)
    if data:
        if method == "POST":
            data = parse.urlencode(data).encode('utf-8')
            req.data=data
        else: #get请求的拼接参数
            data = parse.urlencode(data)
            new_url = url + data
            req.full_url = new_url  #替换url
    #看是否有cookie
    if cookies:
        s = ""
        for k,v in cookies.items():
            s += k+"="+v+";"
        # 更新进headers中
        req.add_header(key='Cookie',val=s[:-1])
        #方式2
        # req.headers['cookie'] = s[:-1]
    # 有代理的情况
    if proxies:
        #构建handler
        proxyhandler = request.ProxyHandler(proxies)
        opener = request.build_opener(proxyhandler,cookiejar_handler)
    else:
        opener = request.build_opener(cookiejar_handler)
    body = opener.open(req,timeout=timeout).read()
    return Response(body)

class Response:
    def __init__(self,body):
        self.body = body
    @property
    def content(self):
        return self.body
    @property
    def text(self):
        try:
            return self.body.decode('utf-8')
        except:
            try:
                return self.body.decode('gbk')
            except:
                return self.body.decode('gb2312')
    # json格式的处理
    def json(self):
        return json.loads(self.body)
    # 压缩流格式的处理
    def unzip(self,encoding='utf-8'):
        return gzip.decompress(self.body).decode(encoding)
    # 获取响应的response
    def cookie(self): # 留给大家
        return cookiejar
    # 基于响应进行xpath匹配
    def xpath(self,rule):
        return etree.HTML(self.text).xpath(rule)