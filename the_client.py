import socket
import threading
from datetime import datetime

port = 56000
host = '10.100.102.19'

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host , port))
print("You are logged in")

nickname = input(client.recv(1024).decode())
client.send(nickname.encode())

def write_image(content):
    file = open('D:\\the_screen.txt' , 'ab')
    file.write(content)
    file.close()

def receive():
    while True:
        try:
            print(client.recv(1024).decode())
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        client.send(f'{nickname} [{current_time}]: {input("")}'.encode())

thread_receive = threading.Thread(target=receive)
thread_receive.start()

thread_write = threading.Thread(target=write)
thread_write.start()
