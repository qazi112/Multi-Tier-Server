
from socket import socket
from ThreadedCode.clientHandler2 import ClientHandler_Thread
ADDRESS = "127.0.0.1"
PORT = 5052
bufsize = 1024
scheme = "utf-8"


with socket() as oneSocket:
    oneSocket.bind((ADDRESS,PORT))
    oneSocket.listen(5)

    print(f"Server 2 Started : {oneSocket.getsockname()}")
    while True:
        client,addr = oneSocket.accept()
        print(f"Client : {addr}")
        clientT = ClientHandler_Thread(client)
        clientT.start()
       


