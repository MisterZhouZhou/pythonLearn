# scrapy 初探

## 1、创建项目
```
 scrapy startproject zwblog
```

zwblog目录结构：
```
   zwblog
      |  scrapy.cfg
      |   zwblog
            | items.py
            | pipelines.py
            | settings.py
            | __init__.py
            | spiders
                | __init__.py
```
zwblog目录文件：

    1 scrapy.cfg： 项目到部署配置文件
    2 zwblog/：项目到python模块
    3 zwblog/items.py: 项目中的item文件，类似model
    4 zwblog/pipelines.py: 项目中的Pipelines文件，用于文件持久化存储
    5 zwblog/settings.py: 项目中的配置文件，插件的配置，pipelines的激活等
    6 zwblog/spiders/: 放置spider代码，添加爬虫解析代码等

## 2、添加blog爬虫类
在`zwblog/spiders/`目录下创建zwblogs_spider.py, 代码如下：
```
# coding:utf-8
import scrapy

# 创建一个Spider类需要继承scrapy.Spider, 并定义name, start_urls,parse
class ZwblogSpider(scrapy.Spider):
    name = 'zwblog'  # 爬虫的名称，启动爬虫时使用
    allowed_domains = ['blog.csdn.net']  # 允许的域名
    start_urls = [
        'https://blog.csdn.net/zww1984774346'
    ]

    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        pass
```

## 3、爬虫的启动
```
    scrapy crawl cnblogs  # crawl cnblogs的含义就是启动名称为'cnblogs'的爬虫
```

## 4、开始解析网页
修改`zwblog/spiders/zwblogs_spider.py`中的parse如下：

```
    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath(".//*[@class='article-item-box csdn-tracking-statistics']")
        # 从每条记录中获取数据
        for paper in papers:
            url = paper.xpath(".//*[@class='']/a/@href").extract_first()
            title = paper.xpath(".//*[@class='']/a/text()").extract()[1]
            time_path = paper.xpath(".//*[@class='info-box d-flex align-content-center']/p")
            time = time_path.xpath(".//*[@class='date']/text()").extract_first()
            content = paper.xpath(".//*[@class='content']/a/text()").extract_first()
            print(url, title, time, content)
```

解析结果：

## 4、定义item
修改`zwblog/items.py`内容如下：
```
class ZwblogItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
```

## 5、使用item
修改`zwblog/spiders/zwblogs_spider.py`中的parse如下：
```
    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath(".//*[@class='article-item-box csdn-tracking-statistics']")
        # 从每条记录中获取数据
        for paper in papers:
            url = paper.xpath(".//*[@class='']/a/@href").extract_first()
            title = paper.xpath(".//*[@class='']/a/text()").extract()[1]
            time_path = paper.xpath(".//*[@class='info-box d-flex align-content-center']/p")
            time = time_path.xpath(".//*[@class='date']/text()").extract_first()
            content = paper.xpath(".//*[@class='content']/a/text()").extract_first()
            from zwblog.items import ZwblogItem
            item = ZwblogItem(url=url, title=title, time=time, content=content)
            yield item
```

使用item解析的结果如下：


## 6、数据持久化

修改`zwblog/pipelines.py`

```
import json
from scrapy.exceptions import DropItem

class ZwblogPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'w')

    '''
        每条记录的存储
        定制完Item Pipeline是无法工作的， 需要进行激活，需要启用一个Item Pipeline组件，将它的类添加到settings.py中的ITEM_PIPELINES中
        ITEM_PIPELINES= {
            'cnblogSpider.pipelines.CnblogspiderPipeline': 300, 300表示执行顺序的优先级，执行顺序从低到高
        }
    '''
    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)

```

## 7、激活数据持久化
修改`zwblog/settings.py`
```
ITEM_PIPELINES = {
   'zwblog.pipelines.ZwblogPipeline': 300,
}
```