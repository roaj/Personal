import math
import encryptionBank as netlib

plainText = "Bluebonnets are beautiful!"

rsaPubKey = netlib.rsaPublicKey()
print("public key = ",rsaPubKey)
rsaPrivKey = netlib.rsaPrivateKey()
print("Private Key = ",rsaPrivKey)
cipherText = netlib.rsaEncrypt(plainText, rsaPubKey)
decyptText = netlib.rsaDecrypt(cipherText, rsaPrivKey)
print("Plaintext:\t" , plainText)
print("Ciphertext:\t" , cipherText)
print("Decrypted Text:\t" , decyptText)