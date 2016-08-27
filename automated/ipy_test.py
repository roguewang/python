#!/usr/bin/env python
# Author:rogue
from IPy import *   # 导入一个模块中的所有方法,可以省去用模块名.方法来使用

ip = IP("192.168.0.0/24")   # 把一个网段赋值给一个对象
print(ip.len())     # ip对象的总个数
# for i in ip:
#     print(i)
ip = IP("")
print(ip.reverseNames())
print(ip.iptype())      # IP类型
print(IP("192.168.1.13").iptype())
print("分隔".center(30,"="))
# 转换格式
print(IP("192.168.1.0").make_net("255.255.255.0"))

