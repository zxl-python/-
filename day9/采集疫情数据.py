import requests
import json
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
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
res = requests.get(url).json()
for province in json.loads(res['data'])['areaTree']:
    for province_data in province['children']:
        sql = "insert into province values(%s,%s)"
        cursor.execute(sql,[province_data['name'],province_data['today']['confirm']])
        conn.commit()
        # print(province_data['name'],province_data['today']['confirm'])

# data = json.loads(res['data'])['chinaTotal']
# print(data)
# sql = 'insert into china_count values(%s,%s,%s,%s)'
# cursor.execute(sql,[data['confirm'],data['heal'],data['dead'],data['suspect']])
# conn.commit()
