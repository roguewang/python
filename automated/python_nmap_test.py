#!/usr/bin/env python
# Author:rogue

import nmap

# 常用类:PortScanner()
# 常用类:PortScannerHostDict()

portscanner = nmap.PortScanner()

portscannerH = nmap.PortScannerHostDict()

scan = portscanner.scan("192.168.24.5", "21,22,80")
print(scan)
print("分隔".center(40, "="))

print(len(scan))    # 键的总数

print(str(scan))

