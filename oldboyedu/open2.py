#!/usr/bin/env python
# Author:rogue
# 文件操作
# 1. 打开文件:open("filename","打开方式")
# 打开方式
# r+:读写,多数用这种
# w+:
# x+:
# a+:
# b:用字节的方式
file = open("db","r+",encoding="utf-8")
data = file.read()
print("1 =", data)
file.write("\nabcdefg2")
file.seek(0,0)  # 以字节来定位
d1 = file.read()
print("2 =", d1)
# 2. 操作文件
# 3. 关闭文件
file.close()
# with open("db") as file:
#     pass
