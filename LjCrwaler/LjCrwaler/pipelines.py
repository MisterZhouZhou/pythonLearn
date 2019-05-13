# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
from scrapy.exceptions import DropItem
from urllib.request import urlretrieve
from scrapy.utils.python import to_bytes
import os
import pymysql

class LianjiaPipeline(object):

    def __init__(self, settings):
        self.host = settings.get('HOST')
        self.port = settings.get('PORT')
        self.user = settings.get('USER')
        self.passwd = settings.get('PASSWD')
        self.db = settings.get('DB')
        self.charset = settings.get('CHARSET')
        self.table = settings.get('TABLE')
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    '''
      链接数据库
    '''
    def open_spider(self, spider):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                    charset=self.charset)

        self.db = self.conn.cursor()

    '''
      关闭数据库
    '''
    def close_spider(self, spider):
        self.db.close()
        self.conn.close()

    '''
        数据存储
        :param item:
        :return:            
    '''
    def save_data(self, item):
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item.keys()))
        insert_sql = "insert into `{}`({})values({})".format(self.table, keys, values)
        try:
            self.db.execute(insert_sql, tuple(item.values()))
            self.conn.commit()
        except Exception as e:
            print(e.args)
            self.conn.rollback()


    def select_data(self, item):
        '''
        判重
        :param item:
        :return:
        '''
        value = item.get('from_url')
        select_sql = "select * from `{}` where from_url='{}';".format(self.table, value)
        try:
            self.db.execute(select_sql)
            res = self.db.fetchall()
            if res:
                return True
            else:
                return False
        except Exception as e:
            print(e.args)
            return False

    def process_item(self, item, spider):
        item['linktel'] = '-'.join(item['linktel'])
        item['region'] = '/'.join(item['region'])
        item['image_urls'] = ','.join(item['image_urls'])
        if not self.select_data(item):
            self.save_data(item)
        return item


#  图片下载
class ImageDownloadPipeline(object):

    def __init__(self, settings):
        self.imagepath = settings.get('IMAGES_STORE')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_item(self, item, spider):
        '''
        图片下载
        :param item:
        :param spider:
        :return:
        '''
        for image in item['image_urls'].split(','):
            #图片命名
            image_guid = hashlib.sha1(to_bytes(image)).hexdigest()
            image_name = '%s.jpg' % (image_guid)

            house_id = item['from_url'].split('/')[-1].replace('.html','')
            file_path = '%s/%s'%(self.imagepath, house_id)

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            image_path = '%s/%s/%s'%(self.imagepath, house_id, image_name)

            if not os.path.exists(image_path):
                urlretrieve(image, image_path)
            else:
                raise DropItem('It exists!')