#!/usr/bin/env python
# Author:rogue
list1 = [1,2,3,4,5,6,7,8,9,'a','c','e',9,9,9,9,9,9,9,99,]
if 9 in list1:
    counts = list1.count(9)
    print('9 is in list1')
    print('共有[%s]个9,' % counts,'位置在:[%s]')
    list2 = list1.copy()
    print(list2)