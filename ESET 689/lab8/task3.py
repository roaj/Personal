import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip = "localhost" 
port = 9999
serversocket.bind((ip, port))
data, addr = serversocket.recvfrom(1024)
##General substitution cipher##

"""
Modify your Caesar cipher or ROT13 code to replace each plaintext character “n” times to the right
modulo 128

"""
#cyphers 

"""
inputs:
    n = number of shifts to the right (int)
    plaintext = user input (string)

outputs:
    ciphertext (string)

"""
def cipher(plaintext, shiftNumber):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext = ciphertext + chr(ord(plaintext[i]) + (shiftNumber % 128))
    print("plaintext = ", plaintext, "\tshift by = ", (shiftNumber % 128),"\tciphertext = ",ciphertext) 
    return ciphertext

def deCipher(cipher, shiftNumber):
    plainText = ""
    for i in range(len(cipher)):
        plainText = plainText + chr(ord(cipher[i]) - (shiftNumber % 128))
    print("cipher = ", cipher, "\tshift by = ", (shiftNumber % 128),"\tciphertext = ",plainText) 
    return plainText

deCipher(cipher("cybersecurity",10),10)
