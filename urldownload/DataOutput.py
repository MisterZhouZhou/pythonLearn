# coding:utf-8
import codecs

class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self, path, data):
        fout = codecs.open(path, 'w+', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        for t_data in data:
            fout.write(str(t_data))
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

    # def output_html(self, **kwargs):
    #     fout = codecs.open('baike.html', 'w', encoding='utf-8')
    #     fout.writer('<html>')
    #     fout.writer('<body>')
    #     for data in self.datas:
    #         fout.writer(data)
    #     fout.writer('</body>')
    #     fout.writer('</html>')
    #     fout.close()