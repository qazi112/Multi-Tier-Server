
from socket import socket
ADDRESS = "127.0.0.1"
PORT = 5053

with socket() as oneSocket:
    oneSocket.bind((ADDRESS,PORT))
    oneSocket.listen(5)
    while True:
        client,addr = oneSocket.accept()
        print(client)

        

