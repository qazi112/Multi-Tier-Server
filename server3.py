from ThreadedCode.clientHandler3 import ClientHandler_Thread
from socket import socket

ADDRESS = "127.0.0.1"
PORT = 5053
bufsize = 1024
scheme = "utf-8"

with socket() as oneSocket:
    oneSocket.bind((ADDRESS,PORT))
    oneSocket.listen(5)
    print(f"Server 3 : {oneSocket.getsockname()}")
    while True:
        client,addr = oneSocket.accept()
        print(f"Client {client.getpeername()}, Connected! ")
        clientT = ClientHandler_Thread(client)
        clientT.start()
        

