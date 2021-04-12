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

def polyEncrypt(plainText,keyword = "gkds"):
    ciphertext = ""
    i = 0
    for letter in plainText:
        asciiLetter = ord(letter) 
        asciiKey = ord(keyword[i])
        addedCipherText = chr((asciiKey + asciiLetter)%128)
        ciphertext = ciphertext + addedCipherText
        i = (i + 1)%len(keyword)
    # print(ciphertext)
    return ciphertext

def polyDecrypt(ciphertext,keyword="gkds"):
    plainText = ""
    i = 0
    for letter in ciphertext: 
        asciiLetter = ord(letter)
        asciiKey = ord(keyword[i])
        addedDecipherText = chr((asciiLetter - asciiKey)%128)
        plainText = plainText + addedDecipherText
        i = (i+1)%len(keyword)
    # print(plainText)
    return plainText

