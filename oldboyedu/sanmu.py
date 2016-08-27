#!/usr/bin/env python
# Author:rogue
i = 1
name = "rogue" if i == 1 else "amour"
print(name)
i = 2
name = "rogue" if i == 1 else "amour"
print(name)

# lambda表达式

result = lambda v1: v1 + 100
# 冒号前是参数(形参),冒号后面是函数体及返回
print(result(100))