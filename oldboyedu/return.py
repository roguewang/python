#!/usr/bin/env python
# Author:rogue


def f1():
    print('do nothing')


def f2(*args):
    print("args = ", args, "type = ", type(args))


def f3(**args):
    print("args = ", args, "type = ", type(args))

# s = f1()

f2(1, 2, 3, 4, 5)

f3(v1 = 'rogue', v2 = 32)

dict1 = {'name': 'rogue', 'age': 18, 'county': 'sh'}

print(dict1, type(dict1))

f3(**dict1)