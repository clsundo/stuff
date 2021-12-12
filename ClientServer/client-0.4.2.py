#client.py
import socket
import threading

nickname = input("Choose your nickname : ").strip()

while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.26" #"localhost" #"127.0.0.1"
port = 5151

my_socket.connect((host, port))
my_socket.send(nickname.encode())

def thread_sending():
    while True:
        message_to_send = input("")
        if message_to_send:
            message_with_nickname = nickname + " > " + message_to_send
            my_socket.send(message_with_nickname.encode())
            
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        
        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
