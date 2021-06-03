# Server 1 is echo server
from socket import socket
from ThreadedCode.clientHandler1 import ClientHandler_Thread

ADDRESS = "127.0.0.1"
PORT = 5051
bufsize = 1024
scheme = "utf-8"

with socket() as oneSocket:
    oneSocket.bind((ADDRESS,PORT))
    oneSocket.listen(5)
    print(f"Server 1 Started : {oneSocket.getsockname()}")

    while True:
        
        client,addr = oneSocket.accept()
        print("Client Connected : ",addr)
        # Thread to handle client
        clientT = ClientHandler_Thread(client)
        clientT.start()
        
        
       


