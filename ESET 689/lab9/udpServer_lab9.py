import socket                                         
import encryptionBank as encryption  

ip = "localhost"                          
port = 9999 
clientKey = ""                   

class server:
      def __init__(self,serverIp = "localhost", port = 9999):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
            self.serverAddr = (serverIp,port)
            self.socket.bind(self.serverAddr)
            self.clientKey = ""
            self.cypherMessage = ""
      def listen(self):
            self.data = self.socket.recv(1024).decode()
            if self.data[:1] == "k":
                  self.clientKey = self.data[1:]
                  print(self.clientKey)
            elif self.data[:1] == "m":
                  self.cypherMessage = self.data[1:]
                  self.cypherMessage = encryption.polyDecrypt(self.cypherMessage,self.clientKey)
                  print(self.cypherMessage)
      
c = server()
while True:
      c.listen()
