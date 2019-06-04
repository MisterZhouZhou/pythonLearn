import web
import os

urls = (
    '/', 'index',
    '/he', 'hello'
)

class index:
    def GET(self):
        os.system('osascript -e \'display notification "通知内容" with title "标题" subtitle "子标题"\'')
        return 'Hello, World!'


class hello:
    def GET(self):
        argvs = web.input()
        if len(argvs) < 2:
            str = 'err'
        else:
            str = 'ok'
            title = argvs.title
            msg = argvs.msg
            os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))
        return str

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()