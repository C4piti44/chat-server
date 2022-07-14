import socket
import threading
import datetime
import pyautogui


def transcript(message):
    file = open("C:\\Users\\amitg\\Desktop\\secret.txt" , 'a')
    file.write(message)
    file.write("\n")
    file.close()


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("0.0.0.0" ,  56000))
server.listen()
print("server is up and running")
transcript(str(datetime.date.today()))


cli_nick = {}     #contians all of the clients and their nicknames{client : nickname}

def broadcast(message):
    for client in cli_nick:
        client.send(message)


def get_client2(dic , nickname):
    for client in dic:
        if (nickname == dic[client]):
            client2 = client
    return client2


def change(sr_client):
    sr_client.send("type the nickname of the user that you would like to talk with".encode())
    nickname = sr_client.recv(1024).decode().split(" " ,2)[2]
    des_client = get_client2(cli_nick , nickname)
    while True:
        try:
            sr_client.send(f"what would you like to send {nickname} in private".encode())
            message = sr_client.recv(1024)
            if(message.decode().split(" " , 2)[2]=="!EXIT"):
                break
            else:
                content = "(whisper)" + message.decode()
                des_client.send(content.encode())

        except:
            sr_client.send(f"An error occurred, you can't message {nickname} please try later.".encode())
            print(f"An error in the connection between {cli_nick[sr_client]} and {nickname}")
            break



def handle(client):
    while True:
        try:
            message = client.recv(1024)
            transcript(message.decode())

            if((message.decode()).split(" " , 2)[2] == "!WHORU"):
                client.send("I am yor father!".encode())
                continue

            if((message.decode()).split(" " , 2)[2] == "!EXIT"):
                raise Exception

            if((message.decode()).split(" " , 2)[2] == "!ONLINE"):
                arr = []
                for nickname in cli_nick.values():
                     arr.append(nickname)
                client.send(str(arr).encode())
                transcript(str(arr))
                continue



            if((message.decode()).split(" " , 2)[2]=="!CHANGE"):
                client.send("!CHANGE".encode())
                change(client)
                client.send("!CHANGE".encode())
                continue
            
            broadcast(message) #this method doesn't need an encode function because the message is already encoded
 
        except:
            nickname = cli_nick[client]
            cli_nick.pop(client)
            client.close()
            message2 = f'{nickname} disconnected!'
            broadcast(message2.encode())
            transcript(message2)
            print(message2)
            
            break

def receive_clients(): #this function receive new connections
    while True:
        client , address = server.accept()
        print(f'{str(address)} connected')
        

        client.send("please choose a nickname ".encode())
        nickname = client.recv(1024).decode()        
        cli_nick[client] = nickname
        message3 = f"the nickname of {address} is {nickname} "
        print(message3)
        transcript(message3)

        broadcast(f'{nickname} has joined the chat'.encode())
        client.send("Welcome, you officially joined my chat hope you will enjoy".encode())


        thread = threading.Thread(target=handle ,args=(client, ))
        thread.start()

receive_clients()
