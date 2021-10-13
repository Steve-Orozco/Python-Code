#!/usr/bin/python3

import socket

host = socket.gethostname()
port = 9900

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.bind((host,port))
sock_.listen(1)

print("\nServer Started...\n")

conn,addr = sock_.accept()

print("\nConnection Established with: ",str(addr))
message = "\nThanks for the Tunnel!" +str(addr)
conn.send(message.encode("ascii"))
conn.close()

