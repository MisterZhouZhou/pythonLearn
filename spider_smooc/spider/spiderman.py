# coding:utf-8
from gevent import monkey;monkey.patch_all()
import config
from config import COURSEURL
from spider.parser import Parser
from spider.downloader import Downloader
from filedeal.file_downloader import File_Downloader
'''
这个类是爬虫的主逻辑
'''

class SpiderMan(object):

    def __init__(self):
        self.downloader = Downloader()  # html下载器
        self.parser = Parser()  # html解析器

    def crawl(self, url, ID):
        '''
        :param url: 需要爬取的url
        :return:
        '''
        # 下载好的html
        html_cont = self.downloader.download(url)
        # 爬取到的视频数据信息
        self.res_datas = self.parser.parser(html_cont, ID)


    def download(self, res_datas):
        '''
        :param res_datas: 视频数据信息列表
        :return:
        '''
        id = 0  # 设置线程的id号，只是为了进度条显示的时候进行分类信息
        for res_data in res_datas:
            downloader = File_Downloader(res_data, id)  # 视频文件下载线程，给每个文件分配一个线程(有点偷懒了)
            id += 1
            config.PERLIST.append(0)  # 百分比列表
            downloader.start()

    def cmdshow_gbk(self):
        print(u'#####################################################################')
        print(u"#慕课网视频抓取器")
        print(u"#到慕课网官网打开想要下载的课程的章节列表页面，查看当前url链接")
        print(u"#例如http://www.imooc.com/learn/615，则课程编号为615")
        print(u"#####################################################################")
        try:
            ID = input('输入要下载的课程编号：')
            url = COURSEURL + str(ID)
            print(u"将要下载的课程链接为:", url)
            print(u'开始解析视频,请稍后:')
            self.crawl(url, ID)
            config.PERSUM = len(self.res_datas) * 100.0  # 总的进度
            print(u'共有%d条视频' % len(self.res_datas))
            print(u"课程名称:%s" % self.res_datas[0].subject)
            for res_data in self.res_datas:
                print(u"----->%s" % res_data.filename)
            state = input('选择清晰度（1：超清UHD，2：高清HD，3：普清SD）：')
            if int(state) not in [1, 2, 3]:
                print(u'输入有误')
                return
            config.STATE = config.CHOOSE[int(state) - 1]
            self.download(self.res_datas)
        except Exception as e:
            print(u'程序炸了', e)
            return