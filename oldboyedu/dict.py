#!/usr/bin/env python
# Author:rogue

dict1 = {
    1: {
        'name':'andy',
        'age':38,
        'county':'GZ'
    },
    2: {
        'name':'qx',
        'age':33,
        'county':'HZ'
    }
}
print(dict1)
print(dict1[1])
print(dict1[1]['name'])
dict1[1]['new index'] = '120576' # 新增一个数据
print(dict1)
print(dict1.values())
print(dict1.items())
print(dict1.keys())
print("分割".center(40,'-'))
print(dict1.setdefault(10,{'name':'rogue','age':'18','county':'SH'}))    # 如果有这个键对应的值,返回这个值,如果没有,就添加一个新的值
print(dict1.values())
#print(dict1.popitem())
print(dict1)
for k,v in dict1.items():   # 效率低,有一个dict转list的过程
    print(k,'-----',v)

for key in dict1:
    print(key,dict1[key])