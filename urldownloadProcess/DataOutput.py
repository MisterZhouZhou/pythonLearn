# coding:utf-8
import codecs
import time

class DataOutput(object):

    def __init__(self):
        self.filepath = 'baike_%s.html' % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.writer('<html>')
        fout.writer('<body>')
        fout.close()

    def output_html(self, path):
        fout = codecs.open(path, 'w', encoding='utf-8')
        for data in self.datas:
            fout.writer(data)
        fout.close()

    def output_end(self, path):
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.writer('</body>')
        fout.writer('</html>')
        fout.close()