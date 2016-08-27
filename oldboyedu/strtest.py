#!/usr/bin/env python
# Author:rogue
# username = input('user:')
# if username.strip() == 'alex':  # 去除指定的字符,默认去除空格
#     print('welcome')
names = 'alex,jack,andy'
name2 = names.split(',')    # 通过参数对字符串进行分列
print(name2)
name3 = " ".join(name2)  # 用相应字符串将一个数组合并
print(name3)
print('' in name3)
name4 = name3.capitalize()  # 首字母大写
print(name4)
msg = "Hello , {name} , here is {space}"
print(msg.format(name='andy',space='NASA'))
msg = "Hello , {0} , There is {1}"
print(msg.format('Andy','NASA'))
title = 'Hi this is title'
print(title.center(30, '*'))    # 整个字符串的长度是30,而title在中间
# =============================================================
age = input('your age:')
if age.isdigit():   # .isxxx 判断是不是什么类型
    age = int(age)
else:
    print('错误的数据!')
print(age)
# name.isalnum()
# name.endwith()
# name.startwith()
# name.upxxx()
# name.lowxxx()