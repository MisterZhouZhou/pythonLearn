import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        return [scrapy.FormRequest('http://www.example.com/login',
                                   formdata={'user': 'json', 'pass': 'secret'}, callback=self.login)]

    def login(self, response):
        pass