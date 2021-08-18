import socket
import threading
import datetime
import requests

host = '127.0.0.1'
port = 14900

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server is hosted at", requests.get('http://ip.42.pl/raw').text)

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        now = datetime.datetime.now()
        client, address = server.accept()
        print(str(now.strftime("%H:%M:%S ")) + "Connected with {}\n".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(str(now.strftime("%H:%M:%S ")) + "Nickname is {}\n".format(nickname))
        broadcast("{} joined!\n".format(nickname).encode('ascii'))
        client.send('\nConnected to server!\n'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
