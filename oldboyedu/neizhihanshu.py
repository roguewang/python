#!/usr/bin/env python
# Author:rogue
n = abs(-1)     # 取绝对值
print(n)    # 1

# all(),any()
# 以下都表示为false: 0,None,"",[],(),{}
# all()是迭代参数,只有参数全为真,才为真
n = all([1,2,3,4])  # 全为真,n为真.
print(n)
n1 = all([1,2,3,4,[]])   # 有一个为假,n为假
print(n1)
print("分隔符".center(30,'='))
# any()也是迭代参数,参数中只要有一个为真,就为真
n = any([1,2,3,4,[]])
print(n)
# True
# False
# =============分隔符==============
# True

print("分隔符".center(30,'='))
# bin() 接收一个值,将其转成2进制
# oct() 接收一个值,将其转为8进制
# hex() 接收一个值,将其转为16进制
print(bin(1000))
print(oct(1000))
print(hex(1000))
# 0b1111101000
# 0o1750
# 0x3e8

n = bytes("领域",encoding="utf-8")
print('n = ' ,n)
print(str(bytes("领域",encoding="utf-8"), encoding="utf-8"))

print("分隔符".center(30,'='))
f3 = 123
print(callable(f3))

print("分隔符".center(30,'='))

s = "print('Hello world')"
run = compile(s,"<string>","exec")
exec(run)