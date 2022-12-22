#Imports Modules
import socket
import time

#Defines Server Values
listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname() #Gets Hostname Of Current Macheine

listensocket.bind(('',Port))

#Opens Server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts Incomming Connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True


#Main
while running:
    message = clientsocket.recv(1024).decode() #Receives Message
    print(message) #Prints Message
    if not message == "":
        time.sleep(5)
    #Closes Server If Message Is Nothing (Client Terminated)
    else:
        clientsocket.close()
        running = False