import scrapy
headers = {
    'user-agent':'baiduspider'
}
class NovelSpider(scrapy.Spider):
    name = 'biquge'
    # start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']
    def start_requests(self):
        start_urls = 'http://www.xbiquge.la/xiaoshuodaquan/'
        yield scrapy.Request(start_urls,headers=headers,callback=self.parse)
    def parse(self, res):
        books = res.xpath('//div[@id="main"]//li/a/@href').getall()
        for book_url in books:
            yield scrapy.Request(book_url,callback=self.parse_book,headers=headers)
    def parse_book(self,res):
        cha_urls = res.xpath('//div[@id="list"]/dl/dd/a/@href').getall()
        cha_urls = ["http://www.xbiquge.la" + url for url in cha_urls]
        for cha_url in cha_urls:
            yield scrapy.Request(cha_url,callback=self.cha_parse,headers=headers)
    def cha_parse(self,res):
        content = res.xpath('//title/text()').getall()
        print(content)

