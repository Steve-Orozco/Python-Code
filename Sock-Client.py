#!/usr/bin/python3

import socket

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.connect((socket.gethostname(),9900))
msg = sock = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))
