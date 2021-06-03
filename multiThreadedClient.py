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

        if(self.service == 1):
            self.echo_server(s)

        elif(self.service == 1):
            self.palindrome_check_server(s)

        elif(self.service == 3):
            self.checkLength_server(s)



    def echo_server(self,server_soc):
        
        pass
    def palindrome_check_server(self,server_soc):
        pass
    def checkLength_server(self,server_soc):
        pass
        
    