#!/usr/bin/env python
# Author:rogue
import pexpect
import sys

# 待测试
child = pexpect.spawn("ssh root@linux-node.example.com")
fout = open("mylog.txt","w")
child.logfile = fout
#child.logfile = sys.stdout

child.expect("password:")

child.sendline("123")    # 输入密码

child.expect("#")

child.sendline("ls /home")

child.expect("#")


