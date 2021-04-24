import socket                                         
import time
import json

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "localhost"
port = 12000                                           
serversocket.bind((host, port))                                  
serversocket.listen()                        

EmployeeInfo = {"Last Name": None,
               "First Name": None,
               "Major": None,
               "Hometown":None,
               "Username": None,
               "Password":None,
               "NULL":None}

# wait for a connection


clientsocket,addr = serversocket.accept() # blocking function

print("Connected to ---> "+addr[0])

for key in EmployeeInfo.keys():
   clientsocket.send(key.encode())
   data = clientsocket.recv(1024) # blocking function
   EmployeeInfo[key] = data.decode()

with open("/home/jorge/exploring/ESET 689/finalProject/temp.txt","+w") as fileOut:
   json.dump(EmployeeInfo,fileOut,indent=4)

clientsocket.close()
