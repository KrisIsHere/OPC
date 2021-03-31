import socket
import threading
import os
from sys import platform
if platform == "linux" or platform == "linux2":
    os.system("rm -rf ")
    os.chdir("tools")
    os.system("cp -r info tools")
elif platform == "darwin":
    print("OPC is currently not supported for mac")
    sys.exit()
elif platform == "win32":
    os.system("clear")
else:
    print("Platform not recognised...")
    sys.exit()


def chat():
        nickname = input("Choose your \033[0;31mnickname\033[97;40m: ")
        server = input("Enter \033[92;40mserver \033[0;31mIP\033[97;40m: ")

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
                message = '\033[0;31m{}\033[97;40m:\033[92;40m {}\033[97;40m'.format(nickname, input(''))
                client.send(message.encode('ascii'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()

def main():
    print("OPC 0.3 | Coded by \033[0;31mKrisIsHere\033[97;40m & \033[0;31mOwenwastaken\033[97;40m")
    xd = input("What would you like to do?: \n\033[92;40m1\033[97;40m) Join \033[92;40m2\033[97;40m) Host \033[92;40m3\033[97;40m) Update: ")
    if xd == "1":
        chat()
    elif xd == "2":
        if platform == "linux" or platform == "linux2":
            os.system("clear")
        elif platform == "darwin":
            print("OPC is currently not supported for mac")
            sys.exit()
        elif platform == "win32":
            os.system("cls")
        if platform == "linux" or platform == "linux2":
            print("Server is up and running!")
            os.system("python3 server.py")
        elif platform == "darwin":
            print("OPC is currently not supported for mac")
            sys.exit()
        elif platform == "win32":
            print("Server is up and running!")
            os.system("server.py")
    elif xd == "3":
        os.chdir('..')
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        #os.system("cp -r tools/.info " + parent)
        os.system("cp -r tools/OPC_update.py " + parent)
        os.system("python3 " + parent + "/OPC_update.py")

if platform == "linux" or platform == "linux2":
    os.system("clear")
    main()
elif platform == "darwin":
    print("OPC is currently not supported for mac")
    sys.exit()
elif platform == "win32":
    os.system("cls")
    main()
else:
    print("Platform not recognised...")
    sys.exit()
