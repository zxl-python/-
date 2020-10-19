import re
def get_headers(s):
    rule = '^(.*?): (.*?)$'
    result = re.findall(rule,s,re.M)
    dict1 = {}
    for value in result:
        dict1[value[0]] = value[1]
    return dict1

# flag:编译标识
# re.S  : 使.可以匹配换行符
# re.I  : 使匹配对大小写不敏感
# re.M : 可以进行多行字符串匹配,会影响^ 和 $
# re.X : 可以把正则规则以多行形式书写

def get_cookies(s):
    res = s.split('; ')
    dict1 = {}
    for data in res:
        n_res = data.split('=')
        dict1[n_res[0]] = n_res[1]
    return dict1

cookie = '''BIDUPSID=65FA57397112A18CB713BD28D24885E2; PSTM=1600827336; BAIDUID=65FA57397112A18C10AE70A415E0C1A2:FG=1; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=69950_0_7_5_10_11_0_0_3_5_3_2_21747_0_0_0_1601192432_0_1601262363%7C9%230_4_1601187476%7C1; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=7506_32617_1431_31254_32794_32723_32230_7517_7605_32115; H_PS_645EC=e7fcrTN8wrYZcCffJ%2FGXtcFcZJPR0Bu%2BuQmcglr6BxyZTyx48fB7fL8Aeyg'''
cookies = get_cookies(cookie)
print(cookies)



