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

# RSA p,q,e,d Variable Set
def rsaVariables():
    p = 47
    q = 71
    e = 97
    d = 1693
    n = p * q
    phiN = (p-1) * (q-1)
    rsaValues = [p,q,e,d,n,phiN]
    return rsaValues

# RSA Public Key Generation
def rsaPublicKey():
    rsaValues = rsaVariables()
    e = rsaValues[2]
    n = rsaValues[4]
    rsaPubKey = [e,n]
    return rsaPubKey

# RSA Private Key Generation
def rsaPrivateKey():
    rsaValues = rsaVariables()
    d = rsaValues[3]
    n = rsaValues[4]
    rsaPrivKey = [d,n]
    return rsaPrivKey

# RSA Encryption Algorithm
def rsaEncrypt(plainText,rsapublicKey):
    e = rsapublicKey[0]
    n = rsapublicKey[1]
    cipherText = [0] * len(plainText)
    i = 0
    for letter in plainText:
         cipherText[i] = (ord(letter) ** e)%n
         i = i + 1
    return cipherText

# RSA Decryption Algorithm
def rsaDecrypt(cipherText,rsaPrivateKey):
    d = rsaPrivateKey[0]
    n = rsaPrivateKey[1]
    plainText = ""
    for letter in cipherText:
        plainValue = (letter ** d)%n
        plainText = plainText + chr(plainValue)
    return plainText