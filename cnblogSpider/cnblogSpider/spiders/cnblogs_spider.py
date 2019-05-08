# coding:utf-8
import scrapy

# 创建一个Spider类需要继承scrapy.Spider, 并定义name, start_urls,parse
class CnblogsSpider(scrapy.Spider):
    # 爬虫启动
    # scrapy crawl cnblogs
    # crawl cnblogs的含义就是启动名称为'cnblogs'的爬虫
    name = 'cnblogs' # 爬虫名称
    allowed_domains = ['cnblogs.com'] # 允许的域名
    start_urls = [
        'http://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]

    # scrapy shell "http://www.cnblogs.com/qiyeboy/default.html?page=1" 获取页面信息
    # response.xpath(".//*[@class='postTitle']/a/text()").extract()  extract()序列化该节点为Unicode字符串并返回list列表

    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有文章
        papers = response.xpath(".//*[@class='day']")
        # 从每篇文章中抽取数据
        print('\n\n\n')
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            item = scrapy.CnblogspiderItem(url=url, title= title, time=time, content=content)
            yield item
        next_page = Selector(response).re(u'<a href="(\S*)*">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)