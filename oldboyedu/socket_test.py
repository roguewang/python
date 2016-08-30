#!/usr/bin/env python
# Author:rogue

import socket


sk = socket.socket()

ip_port = ("127.0.0.1",9998)

sk.bind(ip_port)

sk.listen(5)

conn,addr = sk.accept()

print(addr)

conn.send("welcome..")

conn.close()

