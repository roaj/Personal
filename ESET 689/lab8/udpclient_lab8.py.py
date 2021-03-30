import socket
import task3 as encryption # import task 3 code 

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "localhost"
port = 9999
serverAddr = (ip, port)
cipherShift = 5 
try:
    message2send = input("Message To Server = ") # get message to send from the user
    cipherMessage2send = encryption.cipher(message2send,cipherShift) # encrypt message with subtitution cipher 
    socket.sendto(cipherMessage2send.encode(), serverAddr) # send encrypted message to socket 
    print("Encrypted Message To Server = ",cipherMessage2send) 
    recievedMessage, addr = socket.recvfrom(1024) # receieve response from server 
    print("Message From Server = ",encryption.deCipher(recievedMessage.decode(),cipherShift))
except:
    print("error")

socket.close() # close socket 

    

