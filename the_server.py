import socket
import threading
import datetime


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("0.0.0.0" ,  44444))
server.listen()
print("server is up and running")

clients = []
nicknames = []



def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if((message.decode()).split(" " , 1)[1] == "WHORU"):
                client.send("I am yor father!".encode())
            else:
                broadcast(message)
 
        except:
            index = clients.index(client)
            clients.remove(client)
            print("An error occurred")
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} disconnected!'.encode())
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client , address = server.accept()
        print(f'{str(address)} connected')
        
        client.send("please choose a nickname ".encode())
        nickname = client.recv(1024).decode()        
        clients.append(client)
        nicknames.append(nickname)
        print(f"the nickname of {address} is {nickname} ")
        broadcast(f'{nickname} has joined the chat'.encode())
        client.send("Welcome, you officially joined my chat hope you will enjoy".encode())

        thread = threading.Thread(target=handle ,args=(client,))
        thread.start()


receive()
