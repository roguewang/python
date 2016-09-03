#!/usr/bin/env python
# Author:rogue
import pexpect

ssh_newkey = 'Are you sure you want to continue connecting'
user = "root"
passwd = "123"
host = "linux-node.example.com"
cmd = "mkdir bypython_test"
child = pexpect.spawn("ssh -l %s %s %s" %(user,host,cmd))
child.expect("Password")
child.sendline(passwd)