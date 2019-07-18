from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connection():
    while True:
        client, client_address = SERVER.accept()
        print(f'{client_address} has connected')
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes('{QUIT}', 'utf-8'):
            broadcast(msg, file)


def broadcast(msg, data):
    pass


clients = {}
addresses = {}
HOST = ''
PORT = ''
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == '__main__':
    SERVER.listen(50)
    print('Waiting for connection...')
