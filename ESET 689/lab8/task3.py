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
    ciphertext = "" #initialize string
    for i in range(len(plaintext)):
        ciphertext = ciphertext + chr(ord(plaintext[i]) + (shiftNumber % 128)) #adding shifted letter to the ciphertext string every loop
    print("plaintext = ", plaintext, "\tshift by = ", (shiftNumber % 128),"\tciphertext = ",ciphertext) 
    return ciphertext #return cipher text as a string

def deCipher(cipher, shiftNumber):
    plainText = "" #initialize string
    for i in range(len(cipher)):
        plainText = plainText + chr(ord(cipher[i]) - (shiftNumber % 128)) # adding deShifted letter to the ciphertext string
    return plainText #return decipher text as a string


