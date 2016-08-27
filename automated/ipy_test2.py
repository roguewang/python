#!/usr/bin/env python
# Author:rogue
from IPy import IP

ip_s = input("please input an IP or net-range:")    # 接收用户输入,参数为IP地址或网段地址

ips = IP(ip_s)

if len(ips) > 1:
    print("net: %s" % ips.net())    # 输出网络地址
    print("netmask: %s" % ips.netmask())    # 掩码
    print("broadcast: %s" % ips.broadcast())        # 广播地址
    print("reverse address: %s" % ips.reverseNames()[0])        # 反向解析
    print("subnet: %s" % len(ips))      # 输出子网数
else:   # 为单个ip地址
    print("reverse address: %s" % ips.reverseNames()[0])    # 反向解析

print("hexadecimal: %s" % ips.strHex())     # 16进制
print("binary ip: %s" % ips.strBin())       # 2进制
print("iptype: %s" % ips.iptype())      # 地址类型,如PRIVATE,PUBLIC,LOOPBACK

"""
输出:
please input an IP or net-range:172.16.0.0/24
net: 172.16.0.0
netmask: 255.255.255.0
broadcast: 172.16.0.255
reverse address: 0.16.172.in-addr.arpa.
subnet: 256
hexadecimal: 0xac100000
binary ip: 10101100000100000000000000000000
iptype: PRIVATE
"""
