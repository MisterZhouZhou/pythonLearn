# coding:utf-8
# 网页下载器

import requests

class Downloader(object):
    '''
       这个类主要是下载html
    '''
    def download(self, url):
        if url is None:
            return None
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36', 'host' : 'www.imooc.com'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        return response.text

