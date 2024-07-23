import socket, threading

HOST_IP = socket.gethostbyname(socket.gethostname())

HOST_PORT = 49156

ENCODER = 'utf-8'

BYTESIZE = 1024

#Create a server socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST_IP, HOST_PORT))

server_socket.listen()

# a blank list of client_sockets 

client_socket_list = []

client_name_list = []

def broadcast_message(message):
    '''Send a message to all clients connected to the server'''
    for client in client_socket_list:
        msg = client.send(message.encode(ENCODER))

pass

def receive_message(client_socket):
    '''Receive an incoming message from a specific client and forward the message to be broadcast'''
    
    while True:
        index = client_socket_list.index(client_socket)
        name = client_name_list[index]
        try:
            # get name of given client from list
            
            

            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            print(client_socket)
            message = f"\033[1;92m\t{name}: {message}\033[0m"

            broadcast_message(message)

        except:
            

            client_socket_list.remove(client_socket)

            client_name_list.remove(name)

            client_socket.close()

            broadcast_message(f"\033[5;91m\t{name} has left the chat\033[0m")

            break





    

def connect_client():
    '''Connect an incoming client to the server'''

    print('listening....')
    while True:
        # Accept any incoming client connection
        

        client_socket, client_address = server_socket.accept()

        print(f"Connected with {client_address}...")

        # sen d a name flag to prompt a client for their name

        client_socket.send("NAME".encode(ENCODER))

        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        #Add new client socket and client 

        client_name_list.append(client_name)

        client_socket_list.append(client_socket)

        #update the server, induvidual client, and all clients

        print(f"Name of new client is {client_name}\n")

        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER))

       # client_socket.send(f"{client_name}, you have joined\n".encode(ENCODER))

        broadcast_message(f"{client_name} has joined!\n")

        #Start a thread to receive messages after a connection

        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))

        receive_thread.start()

connect_client()