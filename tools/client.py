import socket
import threading
import os
from sys import platform
import datetime

def chat():
        nickname = input("Choose your \033[0;31mnickname\033[97;40m: ")
        server = input("Enter \033[92;40mserver \033[0;31mIP\033[97;40m: ")
        proxy = input("Proxy (e.g localhost:9050): ")

        proxy1 =  proxy #if this proxy doesnt work and the script gives you an error r>

        os.environ['sock5_proxy'] = proxy1
        os.environ['sock5_proxy'] = proxy1
        os.environ['sock5_proxy'] = proxy1
        os.environ['sock5_PROXY'] = proxy1

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
                message = str(now.strftime("\033[96;40m%H\033[97;40m:\033[96;40m%M\033[97;40m:\033[96;40m%S")) + ' \033[38;2;255;0;211m| \033[0;31m{}\033[97;40m:\033[92;40m {}\033[97;40m'.format(nickname, input(''))
                client.send(message.encode('ascii'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()

chat()
