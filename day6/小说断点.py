'''
小说:断点续传
1. 书籍的url  2. 章节的url
'''
import requests
from lxml import etree
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
# 保存断点
def duandian(book_url,cont_url):
    sql = "update duandian set book_url=%s,cha_url=%s"
    cursor.execute(sql,[book_url,cont_url])
    conn.commit()
# 获取断点
def get_duandian():
    sql = "select * from duandian"
    cursor.execute(sql)
    return cursor.fetchone()
def get_book_url():
    duan_book_url,cont_url = get_duandian()
    url = "http://www.xbiquge.la/xiaoshuodaquan/"
    res = requests.get(url).text
    ele = etree.HTML(res)
    book_urls = ele.xpath('//div[@id="main"]//li/a/@href')
    if duan_book_url == "1": #没断点
        for book_url in book_urls:
            get_chap_url(book_url)
    else: #有断点
        index = book_urls.index(duan_book_url)  #获取索引值
        for book_url in book_urls[index:]: #从断点位置往下
            get_chap_url(book_url,cont_url)
def get_chap_url(book_url,cont_url=None):
    res = requests.get(book_url).text
    ele = etree.HTML(res)
    chapter_urls = ele.xpath('//div[@id="list"]/dl/dd/a/@href')
    if cont_url: #有断点
        index = chapter_urls.index(cont_url) #获取章节索引值
        for chap_url in chapter_urls[index+1:]: #从下一章开始抓取
            get_content(chap_url,book_url)
    else:
        for chap_url in chapter_urls:
            get_content(chap_url,book_url)
def get_content(chap_url,book_url):
    res = requests.get("http://www.xbiquge.la"+chap_url).content.decode('utf-8')
    ele = etree.HTML(res)
    content = ele.xpath('//div[@id="content"]/text()')
    cha_name = ele.xpath('//h1/text()')[0]
    print(cha_name)
    with open("1.txt", "a", encoding="utf-8") as w:
        w.write(cha_name + "\n")
        for cont in content:
            w.write(cont)
        w.write("\n")
    duandian(book_url,chap_url) #写入完毕保存断点
get_book_url()
