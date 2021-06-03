from socket import socket
from threading import Thread
from time import sleep

scheme = "utf-8"
bufsize = 1024

class ClientHandler_Thread(Thread):
    def __init__(self,clientSoc):
        Thread.__init__(self)
        self.clientSoc = clientSoc

    def run(self):
        
        self.clientSoc.send(f"Dear Client of [{self.clientSoc.getsockname()}] Send String.".encode(scheme))
        message = self.clientSoc.recv(bufsize).decode(scheme)

        message = self.check_palindrome(message)
        
        self.clientSoc.send(f"{message}".encode(scheme))
        # close connection
        self.clientSoc.close()

    def check_palindrome(self,string):
        return string == string[::-1]