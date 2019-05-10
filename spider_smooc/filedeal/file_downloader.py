# coding:utf-8
import os, threading, sys, urllib
import config

class File_Downloader(threading.Thread):
    '''
        这个类主要是用来下载视频文件的，继承了线程类
    '''
    def __init__(self, fileInfo, id):
        threading.Thread.__init__(self)
        # 先创建顶层文件夹
        self.__fileInfor = fileInfo
        self.__id = id
        self.createdir()

    def run(self):
        fileurl = self.__fileInfor.url[config.STATE]
        filepath = self.filedir + os.sep + self.__fileInfor.filename.strip() + '.mp4'
        print(fileurl, filepath)
        try:
            urllib.request.urlretrieve(fileurl, filepath, self.Schedule)  # 下载文件
        except Exception as e:
            print(e)

    # 创建顶层文件夹
    def createdir(self):
        # 文件目录 xx(普清)
        self.filedir = self.__fileInfor.subject + "(" + config.INFOR[config.STATE] + ")"
        if os.path.exists(self.filedir) == False:
            os.mkdir(self.filedir)

    #下载任务
    def Schedule(self, blocknum, blocksize, totalsize):
        '''''
        blocknum:已经下载的数据块
        blocksize:数据块的大小
        totalsize:远程文件的大小
        '''
        per = 100.0 * blocknum * blocksize / totalsize
        if per > 100:
            per = 100
        config.LOCK.acquire()
        config.PERLIST[self.__id] = per #记录每个线程的下载百分比，用于计算整个的进度状况
        nowsum = 0  # 当前的进度
        for item in config.PERLIST:
            nowsum += item
        str = u'当前下载进度:---------------->>>>>>>> %.2f%%' % (100*nowsum/config.PERSUM)
        sys.stdout.write(str+"\r")
        sys.stdout.flush()
        config.LOCK.release()

