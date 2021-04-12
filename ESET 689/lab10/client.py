# This is udpclient.py file

#Import libraries
import socket
import pickle
import encryptionBank as encryptionBank

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Set destination port
port = 9999

# Include the server Address 
serverAddr = ('27.0.0.1', port)

# Create Session Key for Session
k = "dlxphw"

# Encrypt Session Key with RSA Algorithm
rsaPubKey = encryptionBank.rsaPublicKey()
encriptedKey = encryptionBank.rsaEncrypt(k,rsaPubKey)
print("Key = ", k, "\tEncrypted Key: ", encriptedKey)

# Send Encrypted Session Key to Server
encriptedKey = pickle.dumps(encriptedKey)
s.sendto(encriptedKey, serverAddr)
keyAcknowledge, addr = s.recvfrom(1024)

# Send message. The string needs to be converted to bytes.
while True:

    # Call to messageSend function for sending message from user input
    print("chat message input = ")
    message = input("-> ")
    messageEncrypt = encryptionBank.polyEncrypt(message,k)
    print("Entered Message: " , message, "\tMessage Encrypted: ", messageEncrypt)
    s.sendto(messageEncrypt.encode(), serverAddr)
    print("Message Sent")

    # Recieve response from server 
    msgReceive, addr = s.recvfrom(1024)
    msgReceive = msgReceive.decode()
    messageDecrypt = encryptionBank.polyDecrypt(msgReceive,k)
    print("Message Received: " , msgReceive, "\tMessage Decrypted: ", messageDecrypt, "\n")

# Close connection
s.close()