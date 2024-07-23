import socket, threading

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 49156
ENCODER = 'utf-8'
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    '''Send a message to a server to be broadcast'''
    
    while True:
        message = input("message...")
        client_socket.send(message.encode(ENCODER))


def receive_message():
    '''Receive a message from an incoming server'''
    while True:
        
        try:
            #Receive an incoming message from the server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            
            if message == "NAME":
                
                name = input("What is your name?:")
                
                client_socket.send(name.encode(ENCODER))   

            else:
                
               # client_socket.send(message.encode(ENCODER))
                print(message)
        except:
            #Close the connection due to error
            
            print("An error has occured, restart client")
            client_socket.close()
            break



#Create to simultaeneously send and receive messages

rec_thread = threading.Thread(target=receive_message)


send_thread = threading.Thread(target=send_message)

#Start the thread

rec_thread.start()
                
send_thread.start()

print("send a message")