# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from utils.write2file import write2file
import os

class ApnerScrapyPipeline(object):
    def process_item(self, item, spider):
        item['poetry_name'] = item['poetry_name'].replace("\n", '')
        item['poetry_author'] = item['poetry_author'].replace("\n", '')
        poetry_content = ""
        for i in item['content']:
            poetry_content += i.replace('\n', '')
        item['content'] = poetry_content

        write2file(item['poetry_name']+" ",item['poetry_author']+" "+item['content'], "data.txt", False)
        return item
