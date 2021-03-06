import math

##Merkle-Hellman Algorithm 
##Private key = super increasing knapsack algorithm
##public Key = general knapsack 

def getPKey(superIncreasingNS,m,n):
    normalNS = []
    for weight in superIncreasingNS:
        key = (weight * n) % m
        normalNS.append(key)
    # print("Public Key = ",normalNS)
    return normalNS

def encryptKnapsack(message,publicKey):
    binaryMessage = []
    cypherText = []
    for letter in message:
        byte = format(ord(letter),'08b')
        binaryMessage.append(byte)
    # print("Binary Message = ",binaryMessage)

    i = 0 
    cypherSum = 0 
    for element in binaryMessage:
        for bit in element:
            individualIteration = int(bit) * publicKey[i]
            cypherSum = cypherSum + individualIteration
            i = (i+1)%len(publicKey)
        cypherText.append(cypherSum)
        cypherSum=0

    # print("Cyphertext = ",cypherText)
    return cypherText

def decrypKnapsack(cypherText,privateKey,m,n):
    modularInverse = pow(n,-1,m)
    # print("modularInverse = ",modularInverse, "modulus = ",m)
    reverseKey = privateKey[::-1]
    # print("reverse key = ",reverseKey)
    
    sum =[]
    for element in cypherText:
        sum.append(element*modularInverse%m) 
    # print("sum = ",sum)

    deCypher = ""
    for sumElement in sum :
        element = ""
        temp = sumElement # so i can manipulate the number
        for key in reverseKey:
            # print("temp = ", temp, "key = ", key )
            if (temp < key):
                element = element + "0"
            else:
                element = element + "1"
                temp = temp - key
        # print(element[::-1])
        element = int(element[::-1],2)
        deCypher = deCypher + chr(element)
    return deCypher

if __name__ == "__main__":
    key = getPKey()
    cypherText = encryptKnapsack("Jorge",key)
    deCypherText = decrypKnapsack(cypherText,superIncreasingNS)
    print(deCypherText)




