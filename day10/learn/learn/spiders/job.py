import scrapy
import re
import json
from ..items import LearnItem
class JobSpider(scrapy.Spider):
    name = 'hehe' # 必写,整个scrapy 启动的项目名称
    # allowed_domains = ['http://wwww.job.com/'] # 允许url的范围只能在该根目录下,一般不做限制
    # start_urls = ['http://www.baidu.com/'] #规定起始的url
    def start_requests(self):  #重载方法,定义scrapy起始请求
        for i in range(1, 100):
            url = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html".format(i)
            yield scrapy.Request(url)
    def parse(self, response): #解析response
        rule = "__SEARCH_RESULT__ = (.*?)</script>"
        job_dict = json.loads(re.findall(rule, response.text)[0])
        for job in job_dict['engine_search_result']:
            yield scrapy.Request(job['job_href'],callback=self.parse1) # 规定该request响应回来的response给那个方法解析
    def parse1(self,res):
        com_name = res.xpath('//p[@class="cname"]/a/@title').getall()[0]
        job_name = res.xpath('//h1/@title').getall()[0]
        item = LearnItem()  # item对象实例化
        item['com_names'] = com_name
        item['job_names'] = job_name
        yield item # 把打包好的item对象yield出去

