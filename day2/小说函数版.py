from urllib import request
import gzip
from lxml import etree
#获取书籍url
def get_book_url(url):
    result = request.urlopen(url).read()
    try:
        res = gzip.decompress(result).decode('utf-8')
    except:
        res = result.decode('utf-8')
    ele = etree.HTML(res)
    book_urls = ele.xpath('//div[@id="main"]//li/a/@href')
    for book_url in book_urls:
        get_cha_url(book_url)
#获取章节url
def get_cha_url(book_url):
    book_res = request.urlopen(book_url).read()
    try:
        book_result = book_res.decode('utf-8')
    except:
        book_result = gzip.decompress(book_res).decode('utf-8')
    ele = etree.HTML(book_result)
    chapter_urls = ele.xpath('//div[@id="list"]/dl/dd/a/@href')
    book_name = ele.xpath('//h1/text()')[0]
    print(book_name)
    new_chapter_urls = ["http://www.xbiquge.la" + url for url in chapter_urls]
    cha_names = ele.xpath('//div[@id="list"]/dl/dd/a/text()')
    for cha_url in new_chapter_urls:
        index = new_chapter_urls.index(cha_url)
        cha_name = cha_names[index]
        get_content(cha_name,cha_url,book_name)
def get_content(cha_name,cha_url,book_name):
    with open(book_name+".txt","a",encoding='utf-8') as w:
        w.write(cha_name+":"+cha_url+"\n")

get_book_url("http://www.xbiquge.la/xiaoshuodaquan/")