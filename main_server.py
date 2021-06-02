from threading import Thread, setprofile
import socket
import time
from multiThreadedClient import MultiThreadClient

# Main server runnning on 
# {"127.0.0.1" : 5050 }
ADDRESS = "127.0.0.1"
PORT = 5050
bufsize = 1024
scheme = "utf-8"
# Services available
servers = {

    1:["127.0.0.1",5051],
    2:["127.0.0.1",5052],
    3:["127.0.0.1",5053]
}
# client_server = { client : server_Number,...}
 
client_server = {}
print(f"Server =>  {ADDRESS} : {PORT}")
print(servers)
with socket.socket() as s:
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        option = int(conn.recv(bufsize).decode(scheme))

        print(f"Client : {addr}, connected! ")
        print(f"Requested Service at : {servers[int(option)]}")
        
        client_server.setdefault(conn,option)
       
        client = MultiThreadClient(conn,servers[int(option)],option)
        client.start()

     
     
        
        