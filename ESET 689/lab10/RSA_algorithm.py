import math
import encryptionBank as bank

plainText = "Bluebonnets are beautiful!"

rsaPubKey = bank.rsaPublicKey()
print("public key = ",rsaPubKey)
rsaPrivKey = bank.rsaPrivateKey()
print("Private Key = ",rsaPrivKey)
cipherText = bank.rsaEncrypt(plainText, rsaPubKey)
decyptText = bank.rsaDecrypt(cipherText, rsaPrivKey)
print("Plaintext:\t" , plainText)
print("Ciphertext:\t" , cipherText)
print("Decrypted Text:\t" , decyptText)
