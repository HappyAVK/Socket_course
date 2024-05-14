#TCP server side
import socket

#Create a server side socket with IPV4 (AF_INET) and TCP(SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


hostname = socket.gethostname()#hostname
ipv4 = socket.gethostbyname(hostname)
print(hostname)#hostname
print(ipv4) #Hostname's ip

#Bind socket to tuple (IP address, Port Address)
server_socket.bind((ipv4, 12345))

#server socket will listen for any possible connections
server_socket.listen()

while True:
    #Accept every connection continuously, store two pieces of info
    client_socket, client_address = server_socket.accept()

    #print(type(client_socket))
    print(client_socket)
    #print(type(client_address))
    print(client_address)

    print(f"Connected to  {client_address}!/n")

    #Send the client socket a message, this needs to be encoded into bytes as you cannot send a string
    client_socket.send("You are connected".encode("utf-8"))

    #close the connetion
    server_socket.close()
    break