#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(attachment)

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Example usage:
send_email('1284564299@qq.com', 'suykvhhlfmuehihh', 'liuyu@maitewang.com', 'Test email', 'Hello, this is a test email!')