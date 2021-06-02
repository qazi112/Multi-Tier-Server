
from socket import socket

ADDRESS = "127.0.0.1"
PORT = 5052
bufsize = 1024
scheme = "utf-8"

def checkPalindrome(data):
    if data == data[::-1]:
        return True
    else:
        return False

with socket() as oneSocket:
    oneSocket.bind((ADDRESS,PORT))
    oneSocket.listen(5)
    print(f"Server 2 Started : {oneSocket.getsockname()}")
    while True:
        client,addr = oneSocket.accept()
        print(f"Client : {addr}")
        message = client.recv(bufsize).decode(scheme)
        message = checkPalindrome(str(message).lower())
        client.send(message.encode(scheme))
        client.close()
       


