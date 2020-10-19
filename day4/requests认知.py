import requests
# r = requests.get('https://www.baidu.com')
# print(r)
# print(r.status_code) #状态码
# print(r.text) #解码后的数据
# print(r.content) #二进制流数据
#乱码的解决方式
# 1.二进制流decode
# print(r.content.decode('utf-8'))
#2. 设置response.encoding 为指定编码
# r.encoding = 'utf-8'
# print(r.text)

# url = "https://www.httpbin.org/post"
# data = {
#     "haha":"heihei",
#     "wenguang":"handsa"
# }
# # res = requests.post(url,data=data).text
# res = requests.post(url,json=data).text
# print(res)

# url = "https://www.httpbin.org/headers"
# url = "https://www.httpbin.org/cookies"
# headers = {
#     "wenguang":"niubi",
#     'bohu':'niubiplus',
#     'cookie':'a=b;c=d;e=f'
# }
# cookies = {
#     'a':'b',
#     'c':'d',
#     'wenguang':'gaga'
# }
# cookies = {'cookie':'a=b;c=d;e=f'} #偶尔行,不推荐
# # res = requests.get(url,headers=headers).text
# res = requests.get(url,cookies=cookies).text
# print(res)

# url = "http://www.httpbin.org/ip"
# proxy = {'http':'http://118.24.88.66:1080'}
# res = requests.get(url,proxies=proxy).text
# print(res)
# res = requests.get(url).text
# print(res)



# response相关内容
for i in range(3):
    url = "https://image.baidu.com/search/acjson?"
    params = {
    'tn':'resultjson_com',
    'logid':'10864871709681075020',
    'ipn':'rj',
    'ct':'201326592',
    'is':'',
    'fp':'result',
    'queryWord':'小狗图片',
    'cl':'2',
    'lm':'-1',
    'ie':'utf-8',
    'oe':'utf-8',
    'adpicid':'',
    'st':'',
    'z':'',
    'ic':'',
    'hd':'',
    'latest':'',
    'copyright':'',
    'word':'小狗图片',
    's':'',
    'se':'',
    'tab':'',
    'width':'',
    'height':'',
    'face':'',
    'istype':'',
    'qc':'',
    'nc':'',
    'fr':'',
    'expermode':'',
    'force':'',
    'pn':'60',
    'rn':'30',
    'gsm':'3c',
    '1601262375626':'',
    }
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
    resp = requests.get(url,params=params,headers=headers)
    print(resp.json())
    resp.close()
# print(resp.url)
# cookies = {"a":"b"}
# cookies.update(resp.cookies) # 更新了cookie
# print(cookies)
# print(resp.request)
