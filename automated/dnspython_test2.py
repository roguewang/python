#!/usr/bin/env python
# Author:rogue
import dns.resolver
import os
import httplib2

"""
实践:DNS域名轮循业务监控
通过DNS轮循技术可以做到一个域名对应多个IP,从而实现最简单且高效的负载平衡,
不过此方案最大的弊端是目标主机不可用时无法被自动删除,因此做好业务主机的服务可用监控至关重要.
本示例通过分析当前域名的解析IP,再结合服务端口探测来实现自动监控,在域名解析中添加,删除Ip时,
无须对监控脚本进行更改.
"""

iplist = []  # 定义域名IP列表 变量
appdomain = "www.baidu.com"  # 定义业务域名


def get_iplist(domain=""):  # 域名解析函数,解析成功Ip将被追加到iplist
    try:
        A = dns.resolver.query(domain, "A")  # 解析A记录类型
    except Exception as e:
        print("dns resolver error..", str(e))
        return
    for i in A:
        iplist.append(i)  # 追加到iplist
    return True


def checkip(ip):
    print("ip = ", ip)
    print("type = ", type(ip))
    checkurl = str(ip) + ":80"
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)
    conn = httplib2.HTTPConnectionWithTimeout(checkurl)

    try:
        conn.request("GET", "/", headers={"Host": appdomain})

        r = conn.getresponse()
        getcontent = r.read(15)

    finally:
        if getcontent == "<!doctype html>":

            print(ip, "[OK]")

        else:
            print(ip, "[Error]")


if get_iplist(appdomain) and len(iplist) > 0:
    for ip in iplist:
        checkip(ip)

else:
    print("dns resolver error...")
