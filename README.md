# Chinese_ancient_poetry_NER

使用Scrapy爬取古诗文网站 https://note.youdao.com/s/DgLg1Pwy

### （1）应用场景与需求

古文语料的命名实体识别将提供大量有价值的古汉语知识，对于古汉语的自然语言处理研究具有重要价值。 课题拟定通过开发实验程序，实现对古诗文网站的数据爬取、分词、实体标注和命名实体识别将原始数据转化为用于知识图谱构建的实体数据集。

### （2）主要研究内容
#### 1）古诗文网站的数据爬取与清洗
- 数据爬取已完成 
- 数据清洗

#### 2）原始语料的实体类型标注
#### 3）命名实体识别模型的设计
### （3）参考
古诗文网站：https://www.gushiwen.cn/

开源的标注工具YEDDA下载地址：https://github.com/jiesutd/YEDDABert-Bilstm-CRF

基线模型：https://github.com/DSXiangLi/ChineseNER


## Scrapy的使用方法

scrapy startproject 项目名

scrapy genspider 爬虫名 域名

scrapy crawl 爬虫名
