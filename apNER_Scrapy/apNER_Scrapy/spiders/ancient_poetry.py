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
    poetries = []
    i = 0

    def parse(self, response):


        block = response.xpath(
            "/html[@id='html']/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='typecont']")
        for i in block:
            print(i.xpath("div[@class='bookMl']/strong").get())
            name_list = i.xpath("span/a")
            for j in name_list:
                poetry = poetry_name_url()
                poetry['name'] = j.xpath('./text()').get()
                poetry['url'] =j.xpath("@href").get()
                print(poetry['name'],poetry['url'])
                self.poetries.append(poetry)
            # https://so.gushiwen.cn/shiwenv_45c396367f59.aspx
            # www.gushiwen.cn/shiwenv_cdc327abcbc1.aspx
        for op in self.poetries:
            print(op['url'])
        yield scrapy.Request(url="https://so.gushiwen.cn"+self.poetries[self.i]['url'], callback=self.parse_p)



    def parse_p(self, response):
        print("Hello")
        content = response.xpath(
            "/html[@id='html']/body/div[@class='main3']/div[@class='left']/div[@id='sonsyuanwen']/div[@class='cont']")
        print(content.xpath("./h1").get())

        if self.i < len(self.poetries):
            self.i += 1
            print("URL____-","https://so.gushiwen.cn"+self.poetries[self.i]['url'])
            yield scrapy.Request(url="https://so.gushiwen.cn" + self.poetries[self.i]['url'], callback=self.parse_p)




