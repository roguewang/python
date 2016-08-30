#!/usr/bin/env python
# Author:rogue

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.85.134", 22, "root", "123", )

# stdin, stdout, stderr = ssh.exec_command("mkdir test")  # 执行命令,获取返回值,访问的应该是登录后用户的home目录

stderr = ssh.exec_command("cd /tmp")
stderr1 = ssh.exec_command("touch abc.sh")
stderr2 = ssh.exec_command("chmod 777 abc.sh")
print(stderr , "\n" , stderr1 , "\n" ,stderr2)


ssh.close()

# 免密码登录

private_ssh_rsa = "/home/rogue/.ssh/id_rsa"

key = paramiko.RSAKey.from_private_key(private_ssh_rsa)

ssh2 = paramiko.SSHClient()

ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect("192.168.85.134",port=22,pkey=key)

ssh2.exec_command("touch efg.sh")

ssh2.close()