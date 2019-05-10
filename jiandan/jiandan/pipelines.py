# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jiandan import settings
import os
import requests


class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_urls']:
            image_url = 'http:'+image_url
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]  # 图片名称
            file_path = '%s/%s' % (dir_path, file_name)
            if os.path.exists(file_name):
                continue

            with open(file_path, 'wb') as file_writer:
                conn = requests.get(image_url)  # 下载图片
                file_writer.write(conn.content)
            file_writer.close()
        return item
