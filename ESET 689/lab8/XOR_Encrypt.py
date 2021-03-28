##CLASS ACTIVITY##


"""
Jorge Roa
ESET 689
"""

def xorEncrypt(plaintext,key):
    ciphertext = ""
    for i in range(len(plaintext)):
        asciiPlaintext = ord(plaintext[i])
        asciiKey = ord(key[i])
        cypherValue = asciiPlaintext ^ asciiKey 
        ciphertext = ciphertext + chr(cypherValue)
    return ciphertext 

message = "wednesday"
key = "EIUTWELKA"
ciphertext = xorEncrypt(message,key)

print("message = ",message,"\n", "key = ",key,"\n", "ciphertext = ",ciphertext)
