#!/usr/bin/env python
# -*-
# Author:rogue

import nmap

nm = nmap.PortScanner()
host = "127.0.0.1"
print("scan:", nm.scan(host, "22-443"))
print("command_line:", nm.command_line())
scaninfo = nm.scaninfo()
print("-----1-----")
# print(nm["127.0.0.1"].hostname())

print(nm[host].state())

print(nm[host].all_protocols())

print(nm[host]["tcp"].keys())


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
