from threading import Thread
import socket
import time

# ========================================

scheme = "utf-8"
bufsize = 1024
# ========================================

class MultiThreadClient(Thread):
    def __init__(self, clientSocket,server,option):
        Thread.__init__(self)
        self.clientSocket = clientSocket
        self.server = server
        self.service = int(option)

    def run(self):
        print(f"In Threaded Client, and this will connect with : {self.server} \n")
        # now become a client of respective server
        s = socket.socket()
        s.connect((self.server[0],int(self.server[1])))
        print(f"Client Thread : {self.clientSocket} : Connected to server 1 \n")
        # ==================================================
        # ask first client to send his message
        self.clientSocket.send("Send Your Message".encode(scheme))
        message = self.clientSocket.recv(bufsize).decode(scheme)  
        
        # send this message to server
          
        s.send(message.encode(scheme))
        message = s.recv(bufsize).decode(scheme)
        s.close()

        self.clientSocket.send(message.encode(scheme))
        
    