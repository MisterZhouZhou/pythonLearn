from urldownload.book import Book

class BookManager(object):
    def __init__(self):
        self.new_book_urls = set() # 未爬取URL集合
        self.old_book_urls = set() # 已爬取URL集合

    def has_new_book(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_book_url_size() != 0

    def get_new_book(self):
        '''
        获取一个未爬取的
        :return:
        '''
        new_book = self.new_book_urls.pop()
        self.old_book_urls.add(new_book)
        return new_book

    def add_book_url(self, book):
        '''
         将新的URL添加到未爬取到URL集合中
        :param url: 单个URL
        :return:
        '''
        if book is None:
            return
        if book not in self.new_book_urls and book not in self.old_book_urls:
            self.new_book_urls.add(book)

    def add_new_book_ulrs(self, books):
        '''
        将新到URL添加到未爬取到URL集合中
        :param urls: URL集合
        :return:
        '''
        if books is None or len(books) ==0:
            return
        for book in books:
            self.add_book_url(book)

    def new_book_url_size(self):
        '''
        获取未爬取到URL集合大小
        :return:
        '''
        return len(self.new_book_urls)

    def old_bookt_url_size(self):
        '''
        获取已爬取到URL集合大小
        :return:
        '''
        return len(self.old_book_urls)