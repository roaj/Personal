import socket                                         
import time
import json
import math
import knapsack as ks
import hashlib


superIncreasingNS = [2,7,11,21,42,89,180,354] #private key 
normalNS = [] #public key

EmployeeInfo = {"Last Name": None,
               "First Name": None,
               "Major": None,
               "Hometown":None,
               "Username": None,
               "Password":None
               }

m = 881 #modulus m should be greater than sum(superIncreasingNS)
n = 588 #multiplier should have no factor in common with modulus

if math.gcd(m,n) != 1:
    raise Exception("n and m are not co-prime")
elif m < sum(superIncreasingNS):
    raise Exception("select a larger multiplier(n)") 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "localhost"
port = 12000                                           
serversocket.bind((host, port))                                  
serversocket.listen()                        

clientsocket,addr = serversocket.accept() # blocking function

print("Connected to ---> "+addr[0])

#getting Public Key (normal knapSack) / put it on Json / send over socket
normalNS = ks.getPKey(superIncreasingNS,m,n)
normalNSJson = json.dumps(normalNS)
clientsocket.send(normalNSJson.encode()) 

for key in EmployeeInfo.keys():
   clientsocket.send(key.encode())
   data = clientsocket.recv(1024) # blocking function
   data = json.loads(data.decode())
   deCypherMessage = ks.decrypKnapsack(data,superIncreasingNS,m,n)
   if key == "Password":
      hash_object = hashlib.sha256(deCypherMessage.encode())
      hex_dig = hash_object.hexdigest()
      EmployeeInfo[key] = hex_dig
   else:
      EmployeeInfo[key] = deCypherMessage


clientsocket.send("done".encode())

clientsocket.close()

with open("./temp.txt","+w") as fileOut:
   json.dump(EmployeeInfo,fileOut,indent=4)

