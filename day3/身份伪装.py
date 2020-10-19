# from urllib import request
# url = "http://www.httpbin.org/cookies"
# headers = {}
# dict2 = {"hehe":"haha"}
# cookies = '''BIDUPSID=65FA57397112A18CB713BD28D24885E2; PSTM=1600827336; BAIDUID=65FA57397112A18C10AE70A415E0C1A2:FG=1; BD_UPN=12314353; BDRCVFR[HHw4GR7hd6D]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; shifen[6904292_77147]=1601170690; BCLID=7167851630412980300; BDSFRCVID=DfIOJexroG3o203rHd8MMaIpWeKK0PjTDYLEwXIw5ir3mHkVNl15EG0PtDR8-Hk-ox_vogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI-5tIvMqRjnbDIhDtIe-mT22-us3IcA2hcHMPoosIOvD605KxkOe-cu5xcjQKTiaKJx2fbUoqRH5p7z5TLtKGbLBPnpBDtD_l5TtUJMsM_9qf7Oqt4bBpjyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHj3XjHrP; COOKIE_SESSION=235809_0_4_4_8_9_0_0_0_4_17_2_235719_0_13_0_1601170685_0_1601170672%7C6%230_0_1601170672%7C1; BD_HOME=1; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=7506_32617_1431_31254_32794_32723_32230_7517_7605_32115; H_PS_645EC=b07eNZLyfpZ5l4lRTWozpV%2FIDfowfpj%2Fy%2ByAXYsg3gt1JOuyELnz0LlxAv0; BDSVRTM=0'''
# s1 = cookies.split('; ')
# dict1 = {}
# for s2 in s1:
#     s3 = s2.split('=')
#     dict1[s3[0]] = s3[1]
# dict1.update(dict2)
# s = ""
# for k,v in dict1.items():
#     s += k+"="+v+";"
# headers['cookie'] = s
# req = request.Request(url,headers=headers)
# res = request.urlopen(req).read().decode()
# print(res)

# 测试人人网登陆
# url = "http://www.renren.com/880792860/profile"
# headers = {'cookie':'t=7af049583d6136bad7a584ed8a5368832;'}
# req = request.Request(url,headers=headers)
# res = request.urlopen(req).read().decode('utf-8')
# with open("renren.html",'w',encoding='utf-8') as w:
#     w.write(res)


# #set-cookie
# from urllib import request
# from http.cookiejar import CookieJar #用户保存在请求的过程中的响应cookie值
# cookiejar = CookieJar() #实例cookiejar对象
# url = "http://www.baidu.com"
# # 构建一个处理器
# handler = request.HTTPCookieProcessor(cookiejar)
# # 构建一个opener
# opener = request.build_opener(handler)
# res = opener.open(url).read().decode('utf-8')
# # 更新cookiejar到请求cookie中
# cookies = {"hehe":"haha"}
# for i in cookiejar:
#     cookies[i.name]=i.value # 更新了原cookie
# print(cookies)
# from myheaders import get_headers
# headers = '''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: BIDUPSID=65FA57397112A18CB713BD28D24885E2; PSTM=1600827336; BAIDUID=65FA57397112A18C10AE70A415E0C1A2:FG=1; BD_UPN=12314353; BDRCVFR[HHw4GR7hd6D]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; shifen[6904292_77147]=1601170690; BCLID=7167851630412980300; BDSFRCVID=DfIOJexroG3o203rHd8MMaIpWeKK0PjTDYLEwXIw5ir3mHkVNl15EG0PtDR8-Hk-ox_vogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI-5tIvMqRjnbDIhDtIe-mT22-us3IcA2hcHMPoosIOvD605KxkOe-cu5xcjQKTiaKJx2fbUoqRH5p7z5TLtKGbLBPnpBDtD_l5TtUJMsM_9qf7Oqt4bBpjyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHj3XjHrP; COOKIE_SESSION=235809_0_4_4_8_9_0_0_0_4_17_2_235719_0_13_0_1601170685_0_1601170672%7C6%230_0_1601170672%7C1; BD_HOME=1; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=44f0yR9uX1%2B%2BvAvtG%2FqjSXp%2BY8OjdYaOMJ2bfySRPyDqUQo2s%2B5ptdXxCJg; H_PS_PSSID=7506_32617_1431_7566_31254_32794_32723_32230_7517_7605_32115; BDSVRTM=0
# Host: www.baidu.com
# Referer: https://www.baidu.com/
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36
# '''
# header = get_headers(headers)
# print(header)

# # 添加代理
# from urllib import request
# url = "http://www.httpbin.org/ip"
# print(request.urlopen(url).read().decode())
# # 不可用的代理:1.时间长不响应(暂定3秒) 2.直接报错 3.响应回来的是本机的ip
# handler = request.ProxyHandler({'http':'123.163.121.57:9999'}) # 构建代理处理器
# # 构建一个opener
# opener = request.build_opener(handler)
# res = opener.open(url,timeout=3).read().decode()
# print(res)


