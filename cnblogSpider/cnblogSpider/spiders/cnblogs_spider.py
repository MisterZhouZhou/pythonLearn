# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess

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
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            from cnblogSpider.items import CnblogspiderItem
            item = CnblogspiderItem(url=url, title= title, time=time, content=content)
            # 请求正文
            request = scrapy.Request(url=url, callback=self.parse_body)
            request.meta['item'] = item # 将item赞存
            yield request
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)

    def parse_body(self, response):
        # 使用Request中的meta属性， 用来将item实例进行暂存
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath(".//img//@src").extract()  # 提取图片链接
        yield item


# if __name__ == '__main__':
#     user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
#     headers = {'User-Agent': user_agent}
#     process = CrawlerProcess(headers)
#     process.crawl(CnblogsSpider)
#     process.start()