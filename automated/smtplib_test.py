#!/usr/bin/env python
# Author:rogue

import smtplib
import string

HOST = "smtp.163.com"
SUBJECT = "test mail send from python"
TO = ""
FROM = ""
text = "test smtplib"
BODY = """
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
),"\r\n")
"""
server = smtplib.SMTP()
server.connect(HOST,"25")   # 通过connect 方法连接smtp主机
# server.starttls()   # 启动安装传输模式
server.login("", "")
server.sendmail(FROM,[TO],BODY)
server.quit()