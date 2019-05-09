# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem

class ZwblogPipeline(object):

    def __init__(self):
        self.file = open('papers.json', 'w')

    '''
        每条记录的存储
        定制完Item Pipeline是无法工作的， 需要进行激活，需要启用一个Item Pipeline组件，将它的类添加到settings.py中的ITEM_PIPELINES中
        ITEM_PIPELINES= {
            'cnblogSpider.pipelines.CnblogspiderPipeline': 300, 300表示执行顺序的优先级，执行顺序从低到高
        }
    '''
    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)
