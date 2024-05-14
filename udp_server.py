import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname() #hostname

IPv4 = socket.gethostbyname(hostname)

server_socket.bind((IPv4, 12345))


#UDP is a connectionless protocol, does not need socket.listen

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))

print(address)