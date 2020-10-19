import requests
from requests.cookies import cookiejar_from_dict
# 维持cookies
cookies = {
    "name":"wenguang",
    'detail':"cool,beautiful-man"
}
url = "http://www.httpbin.org/cookies"
res = requests.get(url,cookies=cookies).text
print(res)
res = requests.get(url).text
print(res)

#实例一个session对象
# s = requests.Session()
# # 给session属性重新赋值
# s.cookies = cookiejar_from_dict(cookies)
# res = s.get(url).text
# print(res)
# res = s.get(url).text
# print(res)

# 维持headers
# url = "http://www.httpbin.org/headers"
# headers = {
#     'user-agent':'huge',
#     'referer':'meishan'
# }
# s = requests.session()
# s.headers = headers
# res = s.get(url,headers={'user-agent':'wenguang','smail':'gagaga'}).text
# print(res)



















