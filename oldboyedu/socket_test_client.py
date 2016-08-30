#!/usr/bin/env python
# Author:rogue

import socket


sk = socket.socket()

ip_port = ("127.0.0.1",9998)

sk.connect(ip_port)

data = sk.recv(1024)

print(data)

sk.close()