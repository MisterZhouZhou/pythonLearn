#coding:utf-8

from flask import Flask,render_template,flash
from flask_mail import Mail, Message
from flask_moment import Moment
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired

'''
这个类描述了网页上的结构
'''
class MailForm(Form):
    receiver = StringField('收件人:', validators=[DataRequired(), Email()])
    style = StringField('主题:', validators=[DataRequired()])
    body = TextAreaField('正文:', validators=[DataRequired()])
    submit = SubmitField('发送')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qiyeboy'
# 下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.163.com'  # 电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = '25'  # 电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True  # 启用传输层安全
app.config['MAIL_USERNAME'] = '16619930394@163.com'  # os.environ.get('MAIL_USERNAME') #邮件账户用户名
app.config['MAIL_PASSWORD'] = 'zw16619930394'  # os.environ.get('MAIL_PASSWORD') #邮件账户的密码/口令密码

mail = Mail(app)
bootstrap = Bootstrap(app)  # 进行网页渲染
moment = Moment(app)  # 时间

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
       flask中的路由
    :return:
    '''
    mailForm = MailForm()  # 表单
    if mailForm.validate_on_submit():  # 表单提交成功的判断
        try:
            receiverName = mailForm.receiver.data  # 收件人文本框的内容
            styledata = mailForm.style.data  # 主题文本框的内容
            bodydata = mailForm.body.data  # 正文文本框的内容
            msg = Message(styledata, sender=app.config['MAIL_USERNAME'], recipients=[receiverName])  # 发件人，收件人
            msg.body = bodydata
            mail.send(msg)
            flash('邮件发送成功!')  # 提示信息
        except:
            flash('邮件发送失败!')

    return render_template('index.html', form=mailForm, name=app.config['MAIL_USERNAME'])  # 渲染网页


if __name__ == '__main__':
    app.run(debug=True)