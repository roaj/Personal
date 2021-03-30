import socket
import encryptionBank as encryption
import time
clientKey = ["gkds","textbook","Tech","Howdy","btrfg"]
messages = ["texas","encyclopedia","engineer", "ESET program", "How are you?"]

class Client:
    def __init__(self,serverIp = "localhost", serverPort = 9999):
        self.serverAddr = (serverIp,serverPort)
        self.clientKey = clientKey[0]
    
    def sendMessage(self,message2send):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.socket.sendto(message2send.encode(),self.serverAddr)
    
    def setKey(self,key):
        self.clientKey = key

    def sendKey(self):
        self.sendMessage("k"+self.clientKey)
    
    def sendEncryptedMessage(self,plainText):
        self.encryptedMessage = encryption.polyEncrypt(plainText,self.clientKey)
        self.sendMessage("m"+self.encryptedMessage)

c = Client("localhost",9999)
for i,message in enumerate(messages):
    c.setKey(clientKey[i])
    c.sendKey()
    c.sendEncryptedMessage(message)
    print("packet sent")
    time.sleep(5)




    

