from multiprocessing.managers import BaseManager

# 创建类似的Queuemanager
class NodeManager():

    def start_Manager(self, url_q, result_q):
        '''
        创建一个分布式管理器
        :param url_q: url队列
        :param result_q: 结果队列
        :return:
        '''
        # 把创建到两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
        # 将Queue对象在网络上暴漏
        BaseManager.register('get_task_queue', callable=lambda :url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        # 绑定端口8001，设置口令'baike', 这个相当于初始化对象
        manager = BaseManager(address=('127.0.0.1', 8001), authkey='baike')
        # 返回manager对象
        return manager
