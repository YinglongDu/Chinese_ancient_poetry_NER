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
    allowed_domains = ["gushiwen.cn"]
    start_urls = ["https://so.gushiwen.cn/gushi/tangshi.aspx"]  # 唐诗300首

    #start_urls = ["https://so.gushiwen.cn/gushi/sanbai.aspx"]
    poetries = []
    i = 0

    def parse(self, response):

        block = response.xpath(
            "/html[@id='html']/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='typecont']")
        for i in block:
            name_list = i.xpath("span/a")
            for j in name_list:
                poetry = poetry_name_url()
                poetry['name'] = j.xpath('./text()').get()
                print(poetry['name'])
                poetry['url'] =j.xpath("@href").get()
                self.poetries.append(poetry)
            # https://so.gushiwen.cn/shiwenv_45c396367f59.aspx
            # www.gushiwen.cn/shiwenv_cdc327abcbc1.aspx
        yield scrapy.Request(url="https://so.gushiwen.cn"+self.poetries[self.i]['url'], callback=self.parse_p)



    def parse_p(self, response):
        item = ApnerScrapyItem()
        content = response.xpath(
            "/html[@id='html']/body/div[@class='main3']/div[@class='left']/div[@id='sonsyuanwen']/div[@class='cont']")
        item['poetry_name'] = content.xpath("./h1/text()").get()
        item['poetry_author'] = content.xpath("./p[@class='source']/a/text()").get()
        item['content'] = content.xpath("./div[@class='contson']/text()").getall()
        yield  item
        if self.i < len(self.poetries):
            self.i += 1
            yield scrapy.Request(url="https://so.gushiwen.cn" + self.poetries[self.i]['url'], callback=self.parse_p)




