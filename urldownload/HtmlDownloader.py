# coding:utf-8
import requests, os

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

    # 获取下载路径
    def getDownloadPath(self, dir_name):
        current_path = os.getcwd() + "/data/{0}".format(dir_name)
        if not os.path.exists(current_path):
            os.makedirs(current_path)
        return current_path