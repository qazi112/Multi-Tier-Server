from threading import Thread
import socket
import time
scheme = 'utf-8'
ADDRESS = "127.0.0.1"
PORT = 5050
bufsize = 1024
s = socket.socket()
s.connect((ADDRESS,PORT))
print("1 -> service 1 , 2 -> service 2 , 3 -> Service 3")

option = input("Select Options 1 , 2 , 3")

s.send(option.encode(scheme))

if(option == "1"):
    print(s.recv(bufsize).decode(scheme))
    message = input("Write your string > ")
    s.send(message.encode(scheme))
    print(s.recv(bufsize).decode(scheme))
elif option == "2":
    pass
elif option == "3":
    pass

# Starts from Here
# response = s.recv(bufsize).decode(scheme)
# print(response)
