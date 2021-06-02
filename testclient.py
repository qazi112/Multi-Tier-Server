from threading import Thread
import socket
import time
scheme = 'utf-8'
ADDRESS = "127.0.0.1"
PORT = 5051
bufsize = 1024
s = socket.socket()
print(s)
s.connect((ADDRESS,PORT))
s.send("asdasd".encode(scheme))
print(s.recv(bufsize).decode(scheme))

