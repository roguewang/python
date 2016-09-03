#!/usr/bin/env python
# Author:rogue

import sys
import nmap
# 此程序失败,原因未确认
scan_row = []

input_data = input("Please input hosts and port:")  # 接收参数,主机名与端口,以空格分隔,端口可以是范围,以-连接

scan_row = input_data.split(" ")    # 将接收到的参数进行分割

if len(scan_row) != 2:      # 判断获取到的参数是否正确
    print("Input Errors!")
    sys.exit(0)

hosts = scan_row[0]     # 将主机名赋值给hosts
port = scan_row[1]      # 将端口赋值给port

try:
    nm = nmap.PortScanner()     # 创建端口扫描对象
except nmap.PortScannerError:   # 报错相关
    print("Nmap not found", sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error!",sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=" -v -sS -p " + port)        # 调用扫描方法
except Exception as e:
    print("Scan error : " ,str(e))

for host in nm.all_hosts():
    print("-".center(40,"-"))       # 好看的分隔符
    print("Host : %s (%s)" % (host, nm[host].hostname()))       # 输出主机及主机名
    print("State : %s " % nm[host].state())     # 输出主机状态,如up,down

    for proto in nm[host].all_protocols():      # 遍历扫描协议,如tcp,udp
        print("------------")
        print("Protocol : %s " % proto)     # 输入协议名

        lport = nm[host][proto].keys()      # 获取协议的所有扫描端口

        lport.sort()        # 排序

        for port in lport:      # 遍历端口及输出端口与状态
            print("port : %s \t state : %s " % (port,nm[host][proto][port]["state"]))
