from bs4 import BeautifulSoup
from proxySpider.entity.proxy_info import ProxyInfo

class HtmlParser(object):

    def parser(self, html_content):
        '''
         用于解析网页内容，抽取URL和数据
        :param page_url:  下载页面的URL
        :param html_content: 下载页面的内容
        :return: 返回URL和数据
        '''
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        tr_nodes = soup.find_all('tr', class_=True)
        proxys = []
        for tr_node in tr_nodes:
            proxy = ProxyInfo()
            i = 0
            for th in tr_node.children:
                if th.string != None and len(th.string.strip()) > 0:
                    if i == 0:
                        proxy.ip = th.string.strip()
                    elif i ==1 :
                        proxy.port = th.string.strip()
                    elif i == 3:
                        proxy.type = th.string.strip()
                    i += 1
            proxys.append(proxy)
        return proxys