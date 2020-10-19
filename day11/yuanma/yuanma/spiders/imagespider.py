import scrapy
from ..items import YuanmaItem
import logging
class LearnSpider(scrapy.Spider):
    name = "img"
    def start_requests(self):
        for pn in range(60, 120, 30):
            uuu = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11460574907095012344&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%8C%AB%E5%92%AA%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30".format(
                pn)
            yield scrapy.Request(uuu)
    def parse(self, response, **kwargs):
        item = YuanmaItem()
        urls = []
        print("你好")
        logging.info(msg="heheda")
        for data in response.json()['data']:
            if data:
                img_url = data['thumbURL']
                urls.append(img_url)
        item['image_urls'] = urls
        yield item
