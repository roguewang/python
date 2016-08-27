#!/usr/bin/env python
# Author:rogue

msg1 = "hello, deer {0}, here is {1}".format("rogue","NASA")
msg2 = "hello, deer {0}, here is {1}".format(*["rogue","Prometheus"])
msg3 = "Hello, Deer {name}, Here is {space}".format(name="Rogue", space="Prometheus")
dic1 = {"name":"Rogue","space":"Prometheus"}
msg4 = "Hello, Deer {name}, Here is {space}".format(**dic1)
print(msg1)
print(msg2)
print(msg3)
print(msg4)