from gevent import monkey
monkey.patch_all()
import requests
import gevent
from gevent.pool import Pool

def run_task(url):
    print('Visit---> %s' % url)
    try:
        response = requests.get(url)
        print('%d bytes received from %s.' %(len(response.text), url))
    except Exception as e:
        print(e)
    return 'url: %s --->finish' % url

def test():
    urls = ['https://github.com', 'https://www.python.org/', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)

if __name__ == '__main__':
    # 并发执行两个线程
    pool = Pool(2)
    urls= ['https://github.com', 'https://www.python.org/', 'http://www.cnblogs.com/']
    # 所有线程执行完后会返回结果列表
    results = pool.map(run_task, urls)
    print(results)
