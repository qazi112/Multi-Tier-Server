from threading import Thread
import socket
import time

ADDRESS = "127.0.0.1"
PORT = 5050

scheme = 'utf-8'
bufsize = 1024

s = socket.socket()
s.connect((ADDRESS,PORT))

# ==================================================
def client_communication():
    print(s.recv(bufsize).decode(scheme))
    message = input("Write your string > ")
    s.send(message.encode(scheme))
    print(s.recv(bufsize).decode(scheme))
# ===================================================

print("1 -> service 1 Echo , 2 -> service 2 Palindrome, 3 -> Service 3 Length")

option = input("Select Options 1 , 2 , 3")

s.send(option.encode(scheme))

if(option == "1"):
    client_communication()
elif option == "2":
    client_communication()
elif option == "3":
    client_communication()

s.close()