# coding:utf-8
import re
from bs4 import BeautifulSoup
from config import DOWNLOAD_URL
from entity.fileinfor import FileInfor
from spider.downloader import Downloader


class Parser(object):
    '''
    html解析器:从中提取出视频信息
    '''
    def __init__(self):
        self.res_data = []  # 用来存放视频信息

    def parser(self, html_cont, ID):
        '''
        :param html_cont: html内容
        :return:
        '''
        if html_cont is None:
            return
        # 使用BeautifulSoup模块对html进行解析
        soup = BeautifulSoup(html_cont, 'html.parser')
        subject = soup.find('div', class_="hd").get_text()
        links = soup.find_all('a', class_='J-media-item')
        html_down = Downloader() # 这个主要是请求视频的真实链接,抓包的时候你就会明白
        # 下面的代码是将视频信息封装成对象添加到res_data列表中
        for link in links:
            fileinfor = FileInfor()
            fileinfor.subject = subject.strip()  # 移除头尾空格
            fileinfor.filename = link.get_text().strip().replace(':', '_').replace("\r\n","").replace(u'开始学习', "").replace(' ', '')
            fileinfor.mid = link['href'].split('/')[2]
            json_str = html_down.download(DOWNLOAD_URL.replace('{}', ID)).replace('\/', '/').encode('utf-8')
            # json解析
            # 解析方法一
            # dic_json = eval(json_str)
            # 解析方法二
            import json
            dic_json=json.loads(json_str)
            if dic_json['data']['result']['mpath'] != False:
                fileinfor.url['L'] = dic_json['data']['result']['mpath'][0]
                fileinfor.url['M'] = dic_json['data']['result']['mpath'][1]
                fileinfor.url['H'] = dic_json['data']['result']['mpath'][2]
                self.res_data.append(fileinfor)
        return self.res_data