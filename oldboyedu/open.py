#!/usr/bin/env python
# Author:rogue
# 文件操作
# 1. 打开文件:open("filename","打开方式")
# 打开方式
# r:只读
# w:只写,打开时会清空文件
# x:如果文件存在就报错,不存在新建后打开可写.
# a:追加
# file = open('db','ab')
file = open('db','ab')
file.write(bytes("abc",encoding="utf-8"))   # 以字节的方式写入文件
# 2. 操作文件
# 3. 关闭文件
file.close()
# with open("db") as file:
#     pass
