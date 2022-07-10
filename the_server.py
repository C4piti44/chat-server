import socket
import threading
import datetime



server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("0.0.0.0" ,  56000))
server.listen()
print("server is up and running")
file = open("C:\\Users\\amitg\\Desktop\\secret.txt" , 'a')
file.write(str(datetime.date.today()))
file.write("\n")
file.close()

cli_nick = {} #contians all of the clients and their nicknames

def broadcast(message):
    for client in cli_nick:
        client.send(message)

def get_client2(dic , nickname):
    for client in dic:
        if (nickname == dic[client]):
            client2 = client
    return client2


#def switch(client):
    client.send("Which user would you like to talk with?".encode())
    nickname = client.recv(1024).decode()
    client2 = get_client2(cli_nick , nickname)
    while True:
        try:
            message = client.recv(1024) #maybe the message should be encoded
            if(message.decode().split(" " , 2)[2]=="EXIT"):
                break
            client2.send(message)
        except:
            client.send(f"An error occurred, you can't message {nickname} please try later.".encode())
            print("An error occurred1")
            break


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if((message.decode()).split(" " , 2)[2] == "WHORU"):
                client.send("I am yor father!".encode())
                pass
            if((message.decode()).split(" " , 2)[2] == "EXIT"):
                raise Exception
            #elif((message.decode()).split(" " , 2)[2]=="CNG"):
                #switch(client)
                #pass
            
            broadcast(message)
 
        except:
            nickname = cli_nick[client]
            cli_nick.pop(client)
            client.close()
            broadcast(f'{nickname} disconnected!'.encode())
            print(f'{nickname} disconnected!')
            file = open("C:\\Users\\amitg\\Desktop\\secret.txt" , 'a')
            file.write(f'{nickname} disconnected!\n')
            file.close()
            break

def receive_clients(): #this function receive new connections
    while True:
        client , address = server.accept()
        print(f'{str(address)} connected')
        

        client.send("please choose a nickname ".encode())
        nickname = client.recv(1024).decode()        
        cli_nick[client] = nickname
        print(f"the nickname of {address} is {nickname} ")
        file = open("C:\\Users\\amitg\\Desktop\\secret.txt" , 'a')
        file.write(f"the nickname of {address} is {nickname} ")
        file.write("\n")
        file.close()

        broadcast(f'{nickname} has joined the chat'.encode())
        client.send("Welcome, you officially joined my chat hope you will enjoy".encode())


        thread = threading.Thread(target=handle ,args=(client, ))
        thread.start()

receive_clients()
