# from urllib import request
# from lxml import etree
# test_url =  "http://www.httpbin.org/ip"
# # 获取本机IP
# local_ip = request.urlopen(test_url).read().decode()
# for page in range(1,5):
#     url = "https://www.kuaidaili.com/free/inha/%s/"%page
#     res = request.urlopen(url).read().decode('utf-8')
#     ele = etree.HTML(res)
#     #匹配类型
#     types = ele.xpath('//td[@data-title="类型"]/text()')
#     # 匹配IP
#     ips = ele.xpath('//td[@data-title="IP"]/text()')
#     # 匹配端口号
#     ports = ele.xpath('//td[@data-title="PORT"]/text()')
#     # 打包成zip
#     dailis = zip(types,ips,ports)
#     #拼接成对应的代理格式
#     # {'type':'ip:port'}
#     dict1 = {}
#     for daili in dailis:
#         dict1[daili[0]] = daili[1]+":"+daili[2]
#         print("开始测试{}".format(dict1))
#         # 构建代理handler
#         proxy_handler = request.ProxyHandler(dict1)
#         opener = request.build_opener(proxy_handler)
#         try:
#             now_ip = opener.open(test_url,timeout=4).read().decode()
#             print(now_ip)
#             if now_ip != local_ip: #
#                 print("代理可用:{}".format(dict1))
#         except:
#             pass
#
#


from urllib import request
from lxml import etree
test_url =  "http://www.httpbin.org/ip"
# # 获取本机IP
local_ip = request.urlopen(test_url).read().decode()
for page in range(1,5):
    url = "http://www.nimadaili.com/gaoni/%s/"%page
    res = request.urlopen(url).read().decode('utf-8')
    ele = etree.HTML(res)
    # 匹配IP
    ips = ele.xpath('//tbody/tr/td[1]/text()')
    #拼接成对应的代理格式
    # {'type':'ip:port'}
    for ip in ips:
        dict1 = {}
        dict1['http'] = ip
        print("开始测试{}".format(dict1))
        # 构建代理handler
        proxy_handler = request.ProxyHandler(dict1)
        opener = request.build_opener(proxy_handler)
        try:
            now_ip = opener.open(test_url,timeout=4).read().decode()
            print(now_ip)
            if now_ip != local_ip: #
                print("代理可用:{}".format(dict1))
        except:
            pass
# {'http': '123.149.137.21:9999'},{'http': '123.169.102.120:9999'},{'http': '115.221.243.167:9999'},{'http': '200.5.203.58:52116'},{'http': '218.66.253.144:80'}
# {'http': '58.220.95.40:10174'},{'http': '58.220.95.44:10174'},{'http': '78.47.16.54:80'},{'http': '58.220.95.54:9400'}
# {'http': '118.163.83.21:3128'},{'http': '51.161.116.223:3128'},{'http': '80.241.222.138:80'}
# {'http': '59.120.117.244:80'},{'http': '91.205.174.26:80'},{'http': '39.106.223.134:80'},{'http': '218.59.139.238:80'}
# {'http': '115.223.7.110:80'},{'http': '195.178.56.33:8080'},{'http': '190.211.81.214:80'}

# ips = [
# {'http': '123.149.137.21:9999'},{'http': '123.169.102.120:9999'},{'http': '115.221.243.167:9999'},{'http': '200.5.203.58:52116'},{'http': '218.66.253.144:80'},
# {'http': '58.220.95.40:10174'},{'http': '58.220.95.44:10174'},{'http': '78.47.16.54:80'},{'http': '58.220.95.54:9400'},
# {'http': '118.163.83.21:3128'},{'http': '51.161.116.223:3128'},{'http': '80.241.222.138:80'},
# {'http': '59.120.117.244:80'},{'http': '91.205.174.26:80'},{'http': '39.106.223.134:80'},{'http': '218.59.139.238:80'},
# {'http': '115.223.7.110:80'},{'http': '195.178.56.33:8080'},{'http': '190.211.81.214:80'}
# ]
#
# with open("ip.txt","r") as r:
#     ips = r.readlines()
# for ip in ips:
#     proxy_handler = request.ProxyHandler(eval(ip))
#     opener = request.build_opener(proxy_handler)
#     try:
#         now_ip = opener.open(test_url,timeout=4).read().decode()
#         print(now_ip)
#         if now_ip != local_ip: #
#             print("代理可用:{}".format(ip))
#             with open("ip.txt","a") as w:
#                 w.write(str(ip)+"\n")
#     except:
#         pass