import requests, time, random
import itchat

'''
  获取图灵消息
'''
def get_response(msg):
    # 这里我们就是在调用别人的api接口 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    KEY_LIST = ['f67c9021fdf3406fa29f9f4d4aff6ae0', '4b4333156b494e4299d5bb52afc73d6e']
    api_url = 'http://www.tuling123.com/openapi/api'
    for api_key in KEY_LIST:
        data = {
            'key': api_key,
            'info': msg,
            'userid': 'wechat-robot',
        }
        try:
            jsonRes = requests.post(api_url, data=data).json()  # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
            # 图片搜索
            if(jsonRes.get('code') == 200000):
                return image_search(jsonRes)
            result = jsonRes.get('text')
            if result.find(u'当天请求次数已用完') != -1:
                continue
            else:
                return result
        # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
        # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        except Exception as e:
            # 将会返回一个None
            print(e)
            return

'''
  给文件助手发送消息
'''
def sendToFileHelper():
    time.sleep(random.randint(1, 2))
    itchat.send("文件助手你好哦", toUserName="filehelper")

# 图片搜索
def image_search(dict):
    return dict['text']+'  '+dict['url']
