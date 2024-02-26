#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

asender = "1284564299@qq.com"
areceiver = "liuyu19951124@163.com"
acc = "liuyu23@asiainfo.com"
asubject = "this is a test "

from_addr = "1284564299@qq.com"
password = "suykvhhlfmuehihh"

msg = MIMEMultipart()
msg['Subject'] = asubject
msg['to'] = areceiver
msg['Cc'] = acc
msg['from'] = "liuyu"

body = "this is a test"

msg.attach(MIMEText(body, 'plain', 'utf-8'))

xlsxpart = MIMEApplication(open('../test.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='fujian')
msg.attach(xlsxpart)

smtp_server = "smtp.qq.com"
server = smtplib.SMTP(smtp_server, 587)
server.set_debuglevel(1)

server.login(from_addr, password)
server.sendmail(from_addr, areceiver.split(',')+acc.split(','), msg.as_string())

server.quit()
