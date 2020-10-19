import scrapy
import json
headers = {'user-agent':'hehewenguang',
           'cookie':'a=b;c=d;e=f;g=o'
           }
cookies = {
'a':'b',
"c":"",
"d":"e"
}
#{'http': '218.59.139.238:80'}
class Learn(scrapy.Spider):
    name = 'learn'
    def start_requests(self):
        for i in range(10):
            url = "https://www.httpbin.org/post"
            # yield scrapy.Request(url,method='post',body=json.dumps({"a":"b"}))  #传json请求体
            yield scrapy.FormRequest(url,formdata={"a":"b"})  #传递form表单
    def parse(self, response, **kwargs):
        print(response.text)
if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['scrapy','crawl','learn'])