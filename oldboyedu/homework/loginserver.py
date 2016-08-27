#!/usr/bin/env python
# Author:rogue
# 编写登录接口：
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
# 思路：判断一个账户输错三次后把名字写入文件

# import getpass

print("欢迎使用XX系统,请您登录!")
userdb = {'andy':'123456','qx':'987654','rogue':'123123'}

while True:
    flag = True
    blockcount = 0
    blockuser = ""
    username = input("请输入您的账号:")
    password = input("请输入您的密码:")
    for u in userdb.items():
        if username == u[0] and password == u[1]:
            print("登录成功,欢迎您:", u[0])
            flag = False
            break
        else:
            print('continue')
            print(userdb)
            blockcount += 1
            blockuser = username
            continue
    if flag == False:
        break
    if blockcount == 3:
        del userdb[blockuser]

    print("很抱歉,您输入的账号或密码有误,请重试~")



