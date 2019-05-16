# coding:utf-8
from proxySpider.spider.html_downloader import HtmlDownloader
from proxySpider.spider.html_parser import HtmlParser
import requests

class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def crawl_book(self, url):
        html = self.downloader.download(url)
        # 协议ip对象
        proxys = self.parser.parser(html)
        self.detect(proxys)

    def detect(self, proxys):
        badNum = 0
        goodNum = 0
        for proxy in proxys:
            proxy_host = proxy.ip + ':' + proxy.port
            proxie = {}
            if proxy.type.lower() == 'http':
                proxie = {'http': proxy_host}
            elif proxy.type.lower() == 'https':
                proxie = {'https': proxy_host}
            print(proxie)
            try:
                response = requests.get('http://httpbin.org/ip', proxies=proxie)
                print(response)
                if response.status_code == 200:
                    goodNum += 1
                    print('good')
                else:
                    badNum += 1
                    print('bad')
            except Exception as e:
                badNum += 1
                print('bad==', e)
                continue



if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl_book('http://www.xicidaili.com/nn/')