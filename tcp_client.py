#TCP Client-side

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to a server located at a specific port/ip (same machine as client in this script)
server_hostname = socket.gethostname()
client_socket.connect((socket.gethostbyname(server_hostname), 12345))

#Receive a message, you must specify the exact number of bytes to receive
message = client_socket.recv(10)

print(message.decode("utf-8"))

#Receive server message, specify bytes to receive

message= client_socket.recv(10)

print(message.decode("utf-8"))

#Close client socket

client_socket.close()