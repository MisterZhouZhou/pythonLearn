# coding:utf-8
import scrapy
from scrapy.selector import Selector

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

