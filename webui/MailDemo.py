# coding:utf8

import smtplib  # 需要用到SMTPLIB库，来进行邮箱的连接
from email.mime.text import MIMEText  # 处理邮件内容的库 email.mime
from email.mime.multipart import MIMEMultipart  # 处理邮件附件，需要导入MIMEMultipart,Header,MIMEBase
from email.mime.multipart import MIMEBase
from email.header import Header
from email.encoders import encode_base64

# 邮箱属性配置
mailserver = 'smtp.qq.com'  # 邮箱服务端URL
username_SendMail = '776503267@qq.com'  # 发件人
username_AuthCode = 'gtluifcawuakbdgb'  # 邮箱发件授权码，有些邮箱没有，是密码
received_Mail = ['776503267@qq.com']  # 收件人，可设置多个，逗号分割

# 定义文本邮件内容
# content = '这是一封测试邮件。'
# email = MIMEText(content, 'plain', 'utf8')  # 纯文本形式的邮件内容定义，通过MIMEText操作
# email['Subject'] = '邮件主题'  # 定义邮件主题
# email['From'] = username_SendMail
# email['To'] = ','.join(received_Mail)  # 收件人

# 定义HTML邮件内容
# content = """
# <p>这是一封HTML邮件</p>
# <p><a href="http://www.baidu.com">点击这里</a></p>
# """
# email = MIMEText(content, 'html', 'utf8')  # 纯文本形式的邮件内容定义，通过MIMEText操作
# email['Subject'] = '邮件主题'  # 定义邮件主题
# email['From'] = username_SendMail
# email['To'] = ','.join(received_Mail)  # 收件人

# 包含附件的邮件配置
email = MIMEMultipart()
email['Subject'] = '邮件主题'  # 定义邮件主题
email['From'] = username_SendMail
email['To'] = ','.join(received_Mail)  # 收件人
# 非图片附件
att = MIMEBase('application', 'octet-stream')  # 附件规范
att.set_payload(open('测试报告.txt', 'rb').read(), 'base64')  # 读取
att.add_header('Content-Disposition', 'attachment', filename=Header('测试报告.txt', 'utf8').encode())  # 转码
encode_base64(att)  # 这个不加也没有乱码
email.attach(att)
# 图片附件
att1 = MIMEBase('application', 'octet-stream')  # 附件规范
att1.set_payload(open('123.jpg', 'rb').read(), 'base64')  # 读取
att1.add_header('Content-Disposition', 'attachment', filename=Header('测试报告.jpg', 'utf8').encode())  # 转码
encode_base64(att)  # 这个不加也没有乱码
email.attach(att1)

# 发送邮件 核心代码
try:
    smtp = smtplib.SMTP_SSL(mailserver, port=465)  # 邮件服务端端口，非QQ邮箱一般使用SMTP即可（端口一般是25），不需要有SSL
    smtp.login(username_SendMail, username_AuthCode)  # 通过授权码连接邮箱
    smtp.sendmail(username_SendMail, ','.join(received_Mail), email.as_string())  # 通过逗号分割多个收件人
    smtp.quit()
    print "邮件已发送。。"
except smtplib.SMTPException:
    print("Error：Fail")
