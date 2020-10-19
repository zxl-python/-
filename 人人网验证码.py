import requests
from lxml import etree
from day8.chaojiying import get_code
from requests.cookies import cookiejar_from_dict
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8'
)
cursor = conn.cursor()
cookies = {'t':'ba5c88b865a1cdb1cff55a3d2bb0a6da2'}
s = requests.session()
s.cookies = cookiejar_from_dict(cookies)
# 存储namecard
def save_id(ids):
    for namecard in ids:
        try:
            sql = 'insert into renren_card values(%s,%s)'
            cursor.execute(sql,[namecard,'0'])  #存储的card状态为未爬取
            conn.commit()
        except:
            pass
# 修改状态
def change_flag(name_card):
    sql = 'update renren_card set flag=1 where namecard=%s'
    cursor.execute(sql,[name_card])
    conn.commit()
# 提取namecard
def get_name_card():
    sql = 'select namecard from renren_card where flag=%s'
    cursor.execute(sql,["0"]) #提取状态为未爬取的数据
    get_content(cursor.fetchone()[0]) # 返回namecard字符串
# 获取数据
def get_content(name_card):
    res = s.get("http://www.renren.com/"+name_card+"/profile").text
    change_flag(name_card) #提取的namecard修改状态为已爬取
    #获取关联用户
    ele = etree.HTML(res)
    try:
        name = ele.xpath('//title/text()')[0]
        print(name)
        if name == "人人网 - 验证码":
            # 获取图片
            img = ele.xpath('//div[@class="optional"]/img/@src')[0]
            res = s.get(img).content
            #验证码破解
            code = get_code(res)
            print(code)
            check_code(code) #验证码传输
        else:
            namecards = ele.xpath('//div[@id="footprint-box"]/ul/li/a/@namecard')
            save_id(namecards)
    except:
        pass
def check_code(code):
    check_url = "http://www.renren.com/validateuser.do"
    data = {
        'id': '975249282',
        'icode': code,
        'submit': '继续浏览',
        'requestToken': '1659531921',
        '_rtk': '2eab70eb'
    }
    s.post(check_url,data=data)
while True:
    get_name_card()

