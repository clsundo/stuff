#server.py
import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5151
#ADDRESS = "127.0.0.1"
ADDRESS = socket.gethostbyname(socket.gethostname())
broadcast_list = []
nickname_list = []

my_socket.bind((ADDRESS, PORT))


def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()

        #global nickname  #Make as global variable to use it everywhere
        nickname = client.recv(1024).decode()
        
        print(f"Client connected {str(client_address)} >> {nickname}")
        broadcast(f"{nickname} joined the chat!")
        nickname_list.append(nickname)
        print(nickname_list)
        broadcast_list.append(client)

        start_listenning_thread(client)
        
        
def start_listenning_thread(client):
    client_thread = threading.Thread(target=listen_thread,args=(client,)) #the list of argument for the function
    client_thread.start()
    print(f"[ACTIVE CONNEXIONS] {threading.activeCount() - 1}")
    
    
def listen_thread(client):
    while True:
        try:
            message = client.recv(1024).decode()
        except Exception:
            print(f"client has been disconnected : \n{client}")
            broadcast(f"A user has disconnected!")
            return
        
        if message:
            print(f"Received message : {message}")
            broadcast(message)
        else:
            print(f"client has been disconnected : \n{client}")
            return
        
        
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : \n{client}")


print(f"Server is running. (IP = {ADDRESS}:{PORT})")
accept_loop()
