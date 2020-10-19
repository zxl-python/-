#正则匹配
# from urllib import request
# import re
# num = 1
# for pn in range(60,180,30):
#     uuu = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11460574907095012344&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30".format(pn)
#     res = request.urlopen(uuu).read().decode('utf-8')
#     rule = 'middleURL":"(.*?)"'
#     img_urls = re.findall(rule,res)
#     for img_url in img_urls:
#         print(img_url)
#         img_res = request.urlopen(img_url).read()
#         with open("./img/"+str(num)+".jpg","wb") as w:
#             w.write(img_res)
#             num += 1

# json格式处理
# from urllib import request
# import json
# num = 1
# for pn in range(60,180,30):
#     uuu = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11460574907095012344&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30".format(pn)
#     res = request.urlopen(uuu).read().decode('utf-8')
#     new_result = json.loads(res)
#     for data in new_result['data']:
#         img_url = data['middleURL']
#         print(img_url)
#         img_res = request.urlopen(img_url).read()
#         with open("./img/"+str(num)+".jpg","wb") as w:
#             w.write(img_res)
#             num += 1
#
# from urllib import request
# num = 1
# for pn in range(60,180,30):
#     uuu = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11460574907095012344&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30".format(pn)
#     res = request.urlopen(uuu).read().decode('utf-8')
#     new_result = eval(res) #注意:只针对简单的字符串处理,可以用eval
#     for data in new_result['data']:
#         img_url = data['middleURL']
#         print(img_url)
#         img_res = request.urlopen(img_url).read()
#         with open("./img/"+str(num)+".jpg","wb") as w:
#             w.write(img_res)
#             num += 1

# dict1 = "{'hello':'world'}"
# d = eval(dict1)
# print(d,type(d))