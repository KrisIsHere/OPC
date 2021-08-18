import socket
import threading
import os
from sys import platform
import datetime

def chat():
        nickname = input("Choose your nickname: ")
        server = input("Enter server IP: ")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, 14900))

        def receive():
            while True:
                try:
                    message = client.recv(1024).decode('ascii')
                    if message == 'NICK':
                        client.send(nickname.encode('ascii'))
                    else:
                        print(message)
                except:
                    print("An error occured!")
                    client.close()
                    break

        def write():
            while True:
                now = datetime.datetime.now()
                message = str(now.strftime("%H:%M:%S")) + ' | {}: {}'.format(nickname, input(''))
                client.send(message.encode('ascii'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()

chat()
