#!/usr/bin/env python
# Author:rogue
import os,sys,string
import smtplib
import base64

mailserver = "smtp.163.com"
username = ""
password = ""

from_addr = ""

to_addr = ""

msg = "test mail by python.smtplib"

svr = smtplib.SMTP(mailserver)

svr.set_debuglevel(1)

svr.docmd("EHLO server")

svr.docmd("AUTH LOGIN")

svr.send(base64.encodestring(username))

svr.getreply()

svr.send(base64.encodestring(password))

svr.getreply()

svr.docmd("MAIL FROM:<%s" % from_addr)

svr.docmd("RCPT TO:<%s>" % to_addr)

svr.docmd("DATA")

svr.send(msg)

svr.send(".")

svr.getreply()

svr.quit()