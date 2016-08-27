#!/usr/bin/env python
# Author:rogue
import dns.resolver

domain = ""
A = dns.resolver.query(domain,"A")  # 指定查询类型为A记录
for i in A.response.answer:     # 通过response.answer获取查询回应信息
    print(i)
    for j in i.items:       # 遍历回应信息
        print(j)        # 输出解析的IP,在python2.x中可以使用print(j.address)


domain2 = ""
MX = dns.resolver.query(domain2, "MX")      # 指定查询类型为MX值
for i in MX:
    print("MX preference = >>", i.preference, "<< mail exchanger = >>", i.exchange, "<<")

domain3 = "baidu.com"   # 只能输入一级域名,输入二级域名或多级域名是错误的.
ns = dns.resolver.query(domain3, "NS")      # 指定查询类型为NS
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())


domain4 = "www.baidu.com"
cname = dns.resolver.query(domain4, "CNAME")        # 指定查询类型为CNAME
for i in cname.response.answer:
    for j in i.items:
        print(j.to_text())