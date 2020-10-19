import scrapy
from ..items import YuanmaItem
from scrapy.pipelines.images import ImagesPipeline
class LearnSpider(scrapy.Spider):
    name = "run"
    # start_urls = ['http://www.httpbin.org/headers']
    def start_requests(self):
        # start_urls = 'http://www.httpbin.org/cookies'
        start_urls = 'https://www.baidu.com'
        # start_urls = 'http://www.google.com'
        yield scrapy.Request(start_urls,meta={"wenguang":"is so beautiful"})
    def parse(self, response, **kwargs):
        # print(response.body)
        # print(response.headers['Set-Cookie'].decode())
        print(response.meta)


