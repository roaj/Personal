import math

##Merkle-Hellman Algorithm 
##Private key = super increasing knapsack algorithm
##public Key = general knapsack 

superIncreasingNS = [2,3,6,13,27,52] #private key 
normalNS = [] #public key 

m = 105 #modulus m should be greater than sum(superIncreasingNS)
n = 31 #multiplier should have no factor in common with modulus

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
    print("\n\n","###DECRYPTION###")
    # pass
    modularInverse = pow(n,-1,m)
    print("modularInverse = ",modularInverse, "modulus = ",m)
    reverseKey = privateKey[::-1]
    # reverseKey = list(reversed(privateKey))
    print("reverse key = ",reverseKey)
    sum =[]
    for element in cypherText:
        sum.append(element*modularInverse%m) 
    print("sum = ",sum)

    for sumElement in sum :
        cypherElement = [] 
        temp = sumElement
        for key in reverseKey:
            if (temp >= key):
                print("0")
            elif (temp < key ):
                print("1")



key = getPKey()
cypherText = encryptKnapsack("Joe",key)

FakecypherText = [174,280,333]
decrypKnapsack(FakecypherText,superIncreasingNS)


# print(" Private key = ",superIncreasingNS,"\n","Public Key = ",normalNS,"\n")

