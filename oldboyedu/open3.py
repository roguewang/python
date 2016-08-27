#!/usr/bin/env python
# Author:rogue
file = open("bak.log","r",encoding="utf-8")
for i in file:
    print(i)
file.close()
with open("bak.log","r",encoding="utf-8") as file1, open("db2","r+",encoding="utf-8") as file2:
    for line in file1:
        new_str = line.replace("星期","周")
        file2.write(new_str)

