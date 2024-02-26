#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 邮箱服务器地址、端口号、用户名、密码等参数
SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587
USERNAME = '1284564299@qq.com'
PASSWORD = 'suykvhhlfmuehihh'

def send_email(subject, body, to, cc=None, bcc=None, attachments=None):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = ', '.join(to)

    if cc:
        msg['Cc'] = ', '.join(cc)
        to += cc

    if bcc:
        to += bcc

    # 设置邮件正文
    body_part = MIMEText(body, 'html')
    msg.attach(body_part)

    # 添加附件
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=attachment.split('/')[-1])
                part['Content-Disposition'] = f'attachment; filename="{attachment.split("/")[-1]}"'
                msg.attach(part)

    # 连接邮箱服务器并发送邮件
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, to, msg.as_string())

if __name__ == '__main__':
    subject = 'Python自动发邮件测试'
    body = '<h1>这是一封Python自动发送的邮件</h1>'
    to = ['liuyu@maitewang.com']
    cc = ['2653610372@qq.com']
    attachments = ['./631525.csv']

    send_email(subject, body, to, cc=cc, attachments=attachments)
