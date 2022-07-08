from concurrent.futures import thread
import socket
import threading

port = 44444
host = '10.100.102.19'

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host , port))
print("You are logged in")

nickname = input(client.recv(1024).decode())
client.send(nickname.encode())

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
            client.send(f'{nickname}: {input("")}'.encode())


thread_receive = threading.Thread(target=receive)
thread_receive.start()

thread_write = threading.Thread(target=write)
thread_write.start()