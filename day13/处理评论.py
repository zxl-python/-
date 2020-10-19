import wordcloud
import numpy as np
from PIL import Image
import MySQLdb
import jieba
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8'
)
cursor = conn.cursor()
sql = 'select * from wyyyy'
cursor.execute(sql)
datas = cursor.fetchall()
s = ""
for data in datas:
    s += data[0].split("：",1)[-1]
res = jieba.lcut(s)
word = " ".join(res)
image = np.array(Image.open('timg.jpg'))
w = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',background_color='white',scale=5,mask=image)
w.generate(word)
w.to_file("词云测试.jpg")