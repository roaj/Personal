# This is tcpserver.py file
import socket                                         

# create a TCP/IP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()
host = "localhost"
print(host)

#set port number for this server
port = 12000                                           

# bind to the port
serversocket.bind((host, port))                                  

# Listen for incoming connections, queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # wait for a connection
   print('waiting for a connection on port ' + str(port) + '\n')
   clientsocket,addr = serversocket.accept()
   print("client socket# is:", clientsocket)
   print("address is",  addr)

   print("Got a connection from " + str(addr))

   # Receive the data of 1024 bytes maximum. The received data is binary data. 
   data = clientsocket.recv(1024)
   print("received: " + data.decode())

   # Send a reply    
   msg = "Hello back!" + "\n"
   clientsocket.send(msg.encode())

   clientsocket.close()
