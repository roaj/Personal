import socket
import task3 as encryption

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "localhost"
port = 9999
serverAddr = (ip, port)
cipherShift = 5 
try:
    message2send = input("Message To Server = ")
    cipherMessage2send = encryption.cipher(message2send,cipherShift)
    socket.sendto(cipherMessage2send.encode(), serverAddr)
    print("Encrypted Message To Server = ",cipherMessage2send)
    recievedMessage, addr = socket.recvfrom(1024)
    print("Message From Server = ",encryption.deCipher(recievedMessage.decode(),cipherShift))
except:
    print("error")
socket.close()

    

