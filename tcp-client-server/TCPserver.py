#!/usr/bin/python3


import socket

#creating the socket object stream
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host ='127.0.0.1'
host = socket.gethostbyname(socket.gethostname())
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("received connection from %s" % str(address))

    message = 'Hello! Thank you for connecting to the server. This an example message to extend data. ' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
