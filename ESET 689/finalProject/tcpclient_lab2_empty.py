import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "localhost"
port = 12000
clientsocket.connect((host, port))
print("Evil Corp New Employee Form","\n","(1) New Registration","\n","(2) Donate Blood")
userInput = input("Selection : ")

while userInput == "1":
    msg = clientsocket.recv(1024)
    print("what is your = " + msg.decode())
    if msg.decode() == "Done":
        break
    answer = input("answer = ")
    clientsocket.send(answer.encode())

# Close connection
clientsocket.close()


