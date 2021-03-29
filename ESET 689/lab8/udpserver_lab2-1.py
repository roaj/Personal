import socket                                         
import task3 as encryption

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "localhost"                          
port = 9999 
serverAddress = (ip, port)                                          
socket.bind(serverAddress)                        
cipherShift = 5
try:
   while True:  
         data, addr = socket.recvfrom(1024)
         deCipherText = encryption.deCipher(data.decode(),cipherShift)
         replyMessage = "roger"
         print("Message From Client = ",deCipherText)
         reply = encryption.cipher(replyMessage,cipherShift)
         sent = socket.sendto(reply.encode(),addr)
except KeyboardInterrupt:
        print('Interrupted')
        socket.close


