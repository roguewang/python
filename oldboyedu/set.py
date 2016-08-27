#!/usr/bin/env python
# Author:rogue
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.difference(s2)  # 找重复,S1中有,但S2中没有的.
s3 = s1.symmetric_difference(s2)    # 对比2个Set,把不重复的都取出来.
# s1.difference_update(s2)   # 对比2个set,把S1中有,但S2中没有的更新到S1中
print(s1)
print(s3)
# s1.discard(2)   # 将某个参数丢弃
# print(s1)
# s1.remove(1)
# print(s1)
print(s1.union(s2))     # 合并
str1 = 'rogue'
s1.update(str1)
print(s1)
print(list())