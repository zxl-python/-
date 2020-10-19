from urllib import request
from lxml import etree
url = "https://maoyan.com/board/4?offset=0"
headers = {'user-agent':'YoudaoBot'}
with open("ip.txt","r") as r:
    ips = r.readlines()
req = request.Request(url=url,headers=headers)
for ip in ips:
    handler = request.ProxyHandler(eval(ip))
    opener = request.build_opener(handler)
    res = opener.open(req).read().decode('utf-8')
    ele = etree.HTML(res)
    # 匹配电影的url
    film_urls = ele.xpath('//p[@class="name"]/a/@href')
    # 拼接完整的电影url
    film_urls = ["https://maoyan.com"+url for url in film_urls]
    print(film_urls)
    # 取出每一个电影url,并发送请求
    for film_url in film_urls:
        res = opener.open(film_url).read().decode('utf-8')
        print(res)
        ele = etree.HTML(res)
        name = ele.xpath('//h1/text()')
        print(name)