import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "localhost"
port = 12000

clientsocket.connect((host, port))

while True:

    msg = clientsocket.recv(1024)#blocking function

    if msg.decode() == "NULL":
        break  
    else:
        print("what is your " + msg.decode())
        answer = input("answer = ")
        clientsocket.send(answer.encode())

# Close connection
clientsocket.close()


