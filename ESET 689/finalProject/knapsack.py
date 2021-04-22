import math

##Merkle-Hellman Algorithm 
##Private key = super increasing knapsack algorithm
##public Key = general knapsack 

superIncreasingNS = [2,7,11,21,42,89,180,354] #private key 
normalNS = [] #public key 

m = 881 #modulus m should be greater than sum(superIncreasingNS)
n = 588 #multiplier should have no factor in common with modulus

if math.gcd(m,n) != 1:
    raise Exception("n and m are not co-prime")
elif m < sum(superIncreasingNS):
    raise Exception("select a larger multiplier(n)") 


def getPKey():
    for weight in superIncreasingNS:
        key = (weight * n) % m
        normalNS.append(key)
    print("Public Key = ",normalNS)
    return normalNS

def encryptKnapsack(message,publicKey):
    binaryMessage = []
    cypherText = []
    for letter in message:
        byte = format(ord(letter),'08b')
        binaryMessage.append(byte)
    print("Binary Message = ",binaryMessage)

    i = 0 
    cypherSum = 0 
    for element in binaryMessage:
        for bit in element:
            individualIteration = int(bit) * publicKey[i]
            cypherSum = cypherSum + individualIteration
            i = (i+1)%len(publicKey)
        cypherText.append(cypherSum)
        cypherSum=0

    print("Cyphertext = ",cypherText)
    return cypherText

def decrypKnapsack(cypherText,privateKey):
    pass


key = getPKey()
cypherText = encryptKnapsack("Joe",key)
decrypKnapsack(cypherText,superIncreasingNS)

# print(" Private key = ",superIncreasingNS,"\n","Public Key = ",normalNS,"\n")

