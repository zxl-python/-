from urllib import request
import gzip
from lxml import etree
url = "http://www.xbiquge.la/xiaoshuodaquan/"
result = request.urlopen(url).read()
try:
    res = gzip.decompress(result).decode('utf-8')
except:
    res = result.decode('utf-8')
ele = etree.HTML(res)
book_urls = ele.xpath('//div[@id="main"]//li/a/@href')
for book_url in book_urls:
    book_res = request.urlopen(book_url).read()
    try:
        book_result = book_res.decode('utf-8')
    except:
        book_result = gzip.decompress(book_res).decode('utf-8')
    ele = etree.HTML(book_result)
    chapter_urls = ele.xpath('//div[@id="list"]/dl/dd/a/@href')
    book_name = ele.xpath('//h1/text()')[0]
    print(book_name)
    new_chapter_urls = ["http://www.xbiquge.la"+url for url in chapter_urls]
    for chapter_url in new_chapter_urls:
        req = request.Request(chapter_url,headers={'user-agent':"baiduSpider"})
        cha_res = request.urlopen(req).read()
        try:
            cha_result = cha_res.decode('utf-8')
        except:
            cha_result = gzip.decompress(cha_res).decode('utf-8')
        ele = etree.HTML(cha_result)
        content = ele.xpath('//div[@id="content"]/text()')
        cha_name = ele.xpath('//h1/text()')[0]
        print(cha_name)
        with open(book_name + ".txt", "a", encoding="utf-8") as w:
            w.write(cha_name+"\n")
            for cont in content:
                w.write(cont)
            w.write("\n")

