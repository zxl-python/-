from day4 import myrequest
from urllib import request
# url = "http://www.httpbin.org/headers"
# url = "http://www.httpbin.org/cookies"
# url = "http://www.httpbin.org/ip"
# headers = {
#     'user-agent':'wenguangspider',
#     'hehe':'heihei',
#     'cookie':'a=b;c=d;e=f'
# }
# cookies = {
#     "a":'b',
#     "hehe":"fashudahu",
#     "jiji":'GG'
# }
# result = myrequest.get(url,headers=headers).decode('utf-8')
# result = myrequest.get(url,cookies=cookies).decode('utf-8')
# result = myrequest.get(url,proxies={'http': '123.56.161.63:80'},timeout=1).decode('utf-8')
# print(result)

# url = "https://www.iqianyue.com/mypost"
# # res = request.urlopen(url,data={}).read().decode()
# # print(res)
# data = {
#     'name':'taishanghuang',
#     'pass':'1234'
# }
# res = myrequest.post(url,data=data).decode()
# print(res)

# get请求

# url = "https://search.51job.com/list/010000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# opener = request.build_opener()
# req = request.Request(url,headers={})
# res = opener.open(req).read().decode('gbk')
# print(res)
# res = myrequest.get(url).decode('gbk')
# print(res)
# url = "https://search.51job.com/list/010000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,1.html?"
# params = {
#     'lang':'c',
#     'postchannel':'0000'
# }
# res = myrequest.get(url,params=params).decode('gbk')
# print(res)
# url = "https://image.baidu.com/search/acjson?"
# import json
# params = {
# 'tn':'resultjson_com',
# 'logid':'10864871709681075020',
# 'ipn':'rj',
# 'ct':'201326592',
# 'is':'',
# 'fp':'result',
# 'queryWord':'小狗图片',
# 'cl':'2',
# 'lm':'-1',
# 'ie':'utf-8',
# 'oe':'utf-8',
# 'adpicid':'',
# 'st':'',
# 'z':'',
# 'ic':'',
# 'hd':'',
# 'latest':'',
# 'copyright':'',
# 'word':'小狗图片',
# 's':'',
# 'se':'',
# 'tab':'',
# 'width':'',
# 'height':'',
# 'face':'',
# 'istype':'',
# 'qc':'',
# 'nc':'',
# 'fr':'',
# 'expermode':'',
# 'force':'',
# 'pn':'60',
# 'rn':'30',
# 'gsm':'3c',
# '1601262375626':'',
# }
# res = myrequest.get(url,params=params).decode('utf-8')
# for data in json.loads(res)['data']:
#     if data:
#         print(data['thumbURL'])


# url = "https://image.baidu.com/search/acjson?"
# import json
# params = {
# 'tn':'resultjson_com',
# 'logid':'10864871709681075020',
# 'ipn':'rj',
# 'ct':'201326592',
# 'is':'',
# 'fp':'result',
# 'queryWord':'小狗图片',
# 'cl':'2',
# 'lm':'-1',
# 'ie':'utf-8',
# 'oe':'utf-8',
# 'adpicid':'',
# 'st':'',
# 'z':'',
# 'ic':'',
# 'hd':'',
# 'latest':'',
# 'copyright':'',
# 'word':'小狗图片',
# 's':'',
# 'se':'',
# 'tab':'',
# 'width':'',
# 'height':'',
# 'face':'',
# 'istype':'',
# 'qc':'',
# 'nc':'',
# 'fr':'',
# 'expermode':'',
# 'force':'',
# 'pn':'60',
# 'rn':'30',
# 'gsm':'3c',
# '1601262375626':'',
# }
# res = myrequest.get(url,params=params).json()
# print(res)
# print(type(res))

# for page in range(1,5):
#     url = "http://www.nimadaili.com/gaoni/%s/"%page
#     res = myrequest.get(url).xpath('//tbody/tr/td[1]/text()')
#     print(res)

# url = "http://www.xbiquge.la/xiaoshuodaquan/"
# res = myrequest.get(url).unzip('utf-8')
# print(res)