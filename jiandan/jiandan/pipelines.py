# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from jiandan import settings
import scrapy
import os
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class JiandanPipeline(ImagesPipeline):
    def get_media_requests(self, item, info): #重写ImagesPipeline   get_media_requests方法
        '''
                :param item:
                :param info:
                :return:
                在工作流程中可以看到，
                管道会得到文件的URL并从项目中下载。
                为了这么做，你需要重写 get_media_requests() 方法，
                并对各个图片URL返回一个Request:
                '''
        for image_url in item['image_urls']:
            image_url = 'http:' + image_url
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        '''

                :param results:
                :param item:
                :param info:
                :return:
                当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败），
                 item_completed() 方法将被调用。
                '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        return item

# class JiandanPipeline(object):
#     def process_item(self, item, spider):
#         dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
#         if not os.path.exists(dir_path):
#             os.makedirs(dir_path)
#         for image_url in item['image_urls']:
#             image_url = 'http:'+image_url
#             list_name = image_url.split('/')
#             file_name = list_name[len(list_name) - 1]  # 图片名称
#             file_path = '%s/%s' % (dir_path, file_name)
#             if os.path.exists(file_name):
#                 continue
#
#             with open(file_path, 'wb') as file_writer:
#                 conn = requests.get(image_url)  # 下载图片
#                 file_writer.write(conn.content)
#             file_writer.close()
#         return item
