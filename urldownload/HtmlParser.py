# coding:utf-8

import re
import urlparser
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser_root(self, html_content):
        '''
         用于解析网页内容，抽取URL和数据
        :param page_url:  下载页面的URL
        :param html_content: 下载页面的内容
        :return: 返回URL和数据
        '''
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        root_content = self._get_new_urls_root(soup)
        return root_content

    def parser(self, page_url, html_content):
        '''
         用于解析网页内容，抽取URL和数据
        :param page_url:  下载页面的URL
        :param html_content: 下载页面的内容
        :return: 返回URL和数据
        '''
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        html_content = self._get_new_urls(soup)
        return html_content

    def _get_new_urls_root(self, soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回新的URL集合
        '''
        content = []
        for mulu in soup.find_all(class_='mulu'):
            h2 = mulu.find('h2')
            if h2 != None:
                h2_title = h2.string
                lisit = []
                for a in mulu.find(class_='box').find_all('a'):
                    href = a.get('href')
                    box_title = a.string
                    lisit.append({'href': href, 'box_title': box_title})
                content.append({'title': h2_title, 'content': lisit})
        return content

    def _get_new_urls(self, soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回新的URL集合
        '''
        [s.extract() for s in soup('script')]
        html_content = soup.find(class_='content-body').find_all('p')
        return html_content[:-1]

