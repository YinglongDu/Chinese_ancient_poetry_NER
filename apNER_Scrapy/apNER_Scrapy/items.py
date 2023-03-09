# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApnerScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    poetry_name = scrapy.Field()
    poetry_author = scrapy.Field()
    content = scrapy.Field()


class poetry_name_url(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()