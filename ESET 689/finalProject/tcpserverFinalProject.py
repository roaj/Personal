import socket                                         
import time

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
               "Password":None}

while True:
   # wait for a connection
   clientsocket,addr = serversocket.accept()
   print("Connected to ---> "+addr[0])
   time.sleep(1)
   for key in EmployeeInfo.keys():
      clientsocket.send(key.encode())
      data = clientsocket.recv(1024)
      EmployeeInfo[key] = data.decode()
      print(EmployeeInfo.values())
      
   clientsocket.send("Done".encode())
   print("\n","Recorded Information","\n",EmployeeInfo)
   break


clientsocket.close()
