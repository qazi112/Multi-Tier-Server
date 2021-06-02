
from socket import socket

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
        print(client)
        message = client.recv(bufsize).decode(scheme)
        client.send(message.encode(scheme))
        client.close()
       


