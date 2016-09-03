#!/usr/bin/env python
# Author:rogue
#!/usr/bin/env python
# -*-
# Author:rogue

import nmap

nm = nmap.PortScanner()     # 创建端口扫描对象
host = "127.0.0.1"      # 设置目标主机
port = "22-443"     # 设置目标端口
nm.scan(host, port)     # 调用扫描方法,参数指定扫描主机及商品,还可以增加arguments来指定扫描方式
print("command_line:", nm.command_line())   # 输出最终扫描的方法文本(大概是这样)
scaninfo = nm.scaninfo()        # 返回nmap扫描信息,以字典形式
print("-----1-----")
# print(nm["127.0.0.1"].hostname())

print(nm[host].state())     # 反回扫描的主机清单,格式为列表

print(nm[host].all_protocols())     # 返回扫描的协议

print(nm[host]["tcp"].keys())       # 查看扫描协议相关的key

# 以下是一些字典测试功能,与实际使用无关
print(type(scaninfo))
print(str(scaninfo))
print("-------2--------")
for key,value in scaninfo.items():
    print(key + ":" + str(value))
print("-------3--------")

dict1 = scaninfo["tcp"]
print(type(dict1))
print("--------4-------")
print(str(dict1))

print("---------5------")
for key,value in dict1.items():
    print(key + ":" + value)
