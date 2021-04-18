# This is tcpclient.py file

import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()
host = "localhost"

# set destination port
port = 12000

# connection to hostname on the port.
clientsocket.connect((host, port))

# send message. The string needs to be converted to bytes.
message = 'Hello!'
clientsocket.send(message.encode())
print("sent: " + message) 

# Receive no more than 1024 bytes
msg = clientsocket.recv(1024)
print("received: " + msg.decode())

# Close connection
clientsocket.close()

