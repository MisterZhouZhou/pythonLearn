# -*- coding: utf-8 -*-
from scrapy import FormRequest
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Request
import json

class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def start_requests(self):
        # 首先进入登录界面
        return [Request('https://www.zhihu.com/signin',
                        callback=self.start_login,
                        meta={'cookiejar': 1})
                ]

    def start_login(self, response):
        print('====')
        print(response)
        # 开始登录
        # self.xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract_first()
        # print('====')
        # print(response)
        # return [FormRequest(
        #     'https://www.zhihu.com/login/phone_num',
        #     method='POST',
        #     meta={'cookiejar': response.meta['cookiejar']},
        #     formdata={
        #         '_xsrf': self.xsrf,
        #         'phone_num': 'xxxx',
        #         'password': 'w',
        #         'captcha_type': 'cn'
        #     },
        #     callback=self.after_login
        # )]

    def after_login(self, response):
        if json.loads(response.body)['msg'].encode('utf-8') == '登录成功':
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
                self.start_urls[0],
                meta={'cookiejar': response.meta['cookiejar']},
                callback=self.parse_user_info,
                errback=self.parse_err,
            )]
        else:
            self.logger.error('登录失败')
            return

    def parse_user_info(self, response):
        print('ddd====', response)


    def parse_err(self, response):
        print('error====', response)