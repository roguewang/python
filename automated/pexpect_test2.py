#!/usr/bin/env python
# Author:rogue
import pexpect

# 简单实现SSH自动登录
# 失败
import pexpect

child = pexpect.spawn("ssh -l %s %s %s", "root", "linux-node.example.com", "mkdir bypython123")
child.expect("Password:")  # 匹配输出内容,判断是否要密码

child.sendline("123")  # 输入密码

# spawn类,以下需测试

# command参数可以是任意已知系统命令
child = pexpect.spawn("/usr/bin/ftp")  # 启动ftp客户端命令
child = pexpect.spawn("/usr/bin/ssh user@example.com")  # 启动ssh
child = pexpect.spawn("ls -latr /tmp")  # 运行ls

# 当子程序需要参数时,还可以使用Python列表来代替参数

child = pexpect.spawn("/usr/bin/ftp", [])
child = pexpect.spawn("/usr/bin/ssh", ["user@example.com"])
child = pexpect.spawn("ls", ["-latr", "/tmp"], timeout=10)  # timeout为等待结果的超时时间

child = pexpect.spawn("/bin/bash -c 'ls -l | grep LOG > logs.txt'")
child.expect(pexpect.EOF)

shell_cmd = "ls -l | grep LOG > logs.txt"
child = pexpect.spawn("/bin/bash", ["-c", shell_cmd])
child.expect(pexpect.EOF)