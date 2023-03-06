import scrapy
from ..items import ApnerScrapyItem, poetry_name_url


class ap_Pipline(object):
    '''爬取网页'''
    def process_item(self, item,spider):
        return item

class ap2txt(object):
    '''爬取网页数据存入txt文本'''
    def process_item(self,item,spider):
        return item



class AncientPoetrySpider(scrapy.Spider):
    name = "ancient_poetry"
    allowed_domains = ["www.gushiwen.cn"]
    start_urls = ["https://so.gushiwen.cn/gushi/tangshi.aspx"]  # 唐诗300首

    def parse(self, response):
        items = ApnerScrapyItem()
        poetries = poetry_name_url()
        block = response.xpath(
            "/html[@id='html']/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='typecont']")
        for i in block:
            print(i.xpath("div[@class='bookMl']/strong").get())
            name_list = i.xpath("span/a")
            for j in name_list:
                poetries['name'] = j.xpath('./text()').get()
                poetries['url'] =j.xpath("@href").get()

                yield poetries