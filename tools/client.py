import threading,socket

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
