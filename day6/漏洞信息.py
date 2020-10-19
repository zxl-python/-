import requests
from lxml import etree
# for i in range(100):
#     url ="https://www.cnvd.org.cn/flaw/list.htm?flag=true"
#     data = {
#     'number':'请输入精确编号',
#     'startDate':'',
#     'endDate':'',
#     'flag':'true',
#     'field':'',
#     'order':'',
#     'max':'100',
#     'offset':'100',
#     }
#     res = requests.post(url,data=data).text
#     ele = etree.HTML(res)
#     name = ele.xpath('//div[@id="flawList"]//tr/td/a/@title')
#     print(len(name))

#另一个路径

# data = {
# 'CSRFToken':'',
# 'cvHazardRating':'',
# 'cvVultype':'',
# 'qstartdateXq':'',
# 'cvUsedStyle':'',
# 'cvCnnvdUpdatedateXq':'',
# 'cpvendor':'',
# 'relLdKey':'',
# 'hotLd':'',
# 'isArea':'',
# 'qcvCname':'',
# 'qcvCnnvdid':'CNNVD或CVE编号',
# 'qstartdate':'',
# 'qenddate':'',
# }
# for i in range(1,500):
#     url = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno={}&repairLd=".format(i)
#     res = requests.post(url,data=data).text
#     ele = etree.HTML(res)
#     name = ele.xpath('//div[@class="fl"]/a/text()')
#     print(name)


# url = 'https://www.cnvd.org.cn/shareData/download/350'
# res = requests.get(url).text
# print(res)

