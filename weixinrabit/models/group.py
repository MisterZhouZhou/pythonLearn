'''
  群组信息
'''
class Group(object):
    def __init__(self, **kwargs):
        """
        init video object
        :param kwargs:
        """
        super().__init__()
        self.user_name = kwargs.get('user_name')
        self.nick_name = kwargs.get('nick_name')
