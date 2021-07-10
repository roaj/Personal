import socket
import time
import json
import knapsack as ks

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "localhost"
port = 12000
serverPublicKey = []

try:
    clientsocket.connect((host, port))
    serverPublicKey = clientsocket.recv(1024) #blocking
    serverPublicKey = json.loads(serverPublicKey.decode())
    print("Server public key = ",serverPublicKey)
except ConnectionRefusedError:
    print("Server is not online")

while True:

    msg = clientsocket.recv(1024) #blocking function

    if msg.decode() == "done":
        break  
    else:
        while True:
            print("what is your " + msg.decode())
            answer = input("answer = ")
            if answer != "":
                cypherMessage = ks.encryptKnapsack(answer,serverPublicKey)
                cypherMessageJson = json.dumps(cypherMessage)
                print("cypherMessage = ",cypherMessage)
                clientsocket.send(cypherMessageJson.encode())
                break
            else:
                raise Exception("Error[420] - Invalid Input")

# Close connection
clientsocket.close()


