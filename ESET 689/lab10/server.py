# This is udpserver.py file

#Import libraries
import socket
import pickle
import encryptionBank as encryptionBank

# create a UDP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Get local machine address
ip = "127.0.0.1"                          

# Set port number for this server
port = 9999                                           

# Bind to the port
serversocket.bind((ip, port))                                  

# Retreive RSA Keys
rsaPubKey = encryptionBank.rsaPublicKey()
rsaPrivKey = encryptionBank.rsaPrivateKey()

# Receive Encrypted Session Key Message from Client
sessionKey_Encrypt, addr = serversocket.recvfrom(1024)
sessionKey_Encrypt = pickle.loads(sessionKey_Encrypt)

# Decrypt Encrypted Message with Private Key to determine Session Key
sessionKey = encryptionBank.rsaDecrypt(sessionKey_Encrypt,rsaPrivKey)
print("\nEncrypted Key = ", sessionKey_Encrypt, "\tDecrypted Key =  ", sessionKey)

while True:  
   
   # Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
   data, addr = serversocket.recvfrom(1024)
   data = data.decode()
   decryptdata = encryptionBank.polyDecrypt(data,sessionKey)
   print("Message Received: " , data, "\tMessage Decrypted: ", decryptdata)

   # Encrypt and send reply message from user input
   print("Send a reply")
   message = input("-> ")
   messageEncrypt = encryptionBank.polyEncrypt(message,sessionKey)
   print("Entered Message: " , message, "\tMessage Encrypted: ", messageEncrypt)
   serversocket.sendto(messageEncrypt.encode(), addr)