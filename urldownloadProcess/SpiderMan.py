# coding:utf-8

from urldownload.BOOKManager import BookManager
from urldownload.HtmlDownloader import HtmlDownloader
from urldownload.HtmlParser import HtmlParser
from urldownload.DataOutput import DataOutput
from urldownload.book import Book


class SpiderMan(object):

    def __init__(self):
        self.manager = BookManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl_book(self, root_url):
        # 添加入坑URL
        # 获取主页数据
        html = self.downloader.download(root_url)
        html_content = self.parser.parser_root(html)
        for item in html_content:
            book_title = item['title']
            self.downloader.getDownloadPath(book_title)
            for item_item in item['content']:
                href = item_item['href']
                box_title = item_item['box_title']
                book = Book(
                    chapter=book_title,
                    section=box_title,
                    url=href
                )
                self.manager.add_book_url(book)

        while (self.manager.has_new_book() and self.manager.old_bookt_url_size() < 500):
            try:
                # 从URL管理器获取新的url
                book = self.manager.get_new_book()
                # HTML下载器下载网页
                html = self.downloader.download(book.url)
                # HTML解析器抽取网页数据
                data = self.parser.parser(book.url, html)
                self.output.store_data(data)
                path = self.downloader.getDownloadPath(book.chapter) + '/' + book.section + '.html'
                self.output.output_html(path, data)
                print(book.chapter,'/', book.section, '拉取完成')
            except Exception as e:
                # 失败后是否需要重试，根据需求
                # self.manager.add_book_url(book)
                print(book.chapter, '/', book.section, '拉取失败')


    def crawl(self, root_url):
        # 添加入坑URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中国呢是否有新的url, 同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100 ):
            try:
                # 从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url, html)
                # 将抽取到url添加到ULR管理器中
                self.manager.add_new_ulrs(new_urls)
                # 将数据存储到文件
                self.output.store_data(data)
            except Exception as e:
                print('crawl failed')
            self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl_book('http://seputu.com/')