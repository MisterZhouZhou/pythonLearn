class Book(object):

    def __init__(self, **kwargs):
        # super.__init__()
        self.chapter = kwargs.get('chapter')  # 所在章节
        self.section = kwargs.get('section')  # 所在节
        self.url = kwargs.get('url')      # 文章url