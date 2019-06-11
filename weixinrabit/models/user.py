'''
  用户信息
'''
class User(object):
    def __init__(self, **kwargs):
        """
        init video object
        :param kwargs:
        """
        super().__init__()
        self.user_name = kwargs.get('user_name')
