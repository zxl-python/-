import execjs
# js = '''
# function hehe(price){
#     price = price + 1000
#     return price
# }
# '''
# func = execjs.compile(js)
# print(func.call('hehe',1000))

with open('hangkong.js','r') as r:
    js = r.read()
s = execjs.compile(js)
print(s.call('get_data', 'wenguang'))