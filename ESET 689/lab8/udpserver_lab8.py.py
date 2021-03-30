import socket                                         
import task3 as encryption # import task 3 code 

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "localhost"                          
port = 9999 
serverAddress = (ip, port)                                          
socket.bind(serverAddress)                        
cipherShift = 5
try:
   while True:  
         data, addr = socket.recvfrom(1024) #recieve data from socket 
         deCipherText = encryption.deCipher(data.decode(),cipherShift) #decipher recieved data 
         replyMessage = "roger" # make reply message 
         print("Message From Client = ",deCipherText) 
         reply = encryption.cipher(replyMessage,cipherShift) #encrypt reply
         sent = socket.sendto(reply.encode(),addr) #send encrypet reply back to client 
except KeyboardInterrupt:
        print('Interrupted')
        socket.close


