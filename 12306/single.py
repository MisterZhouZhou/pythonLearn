
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, *kwargs)
        return _instance[cls]

    return _singleton

@Singleton
class A(object):
    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    a = A(12)
    print(a.x)