import socket
import threading
import pickle

games = {'ABCD': [True, False, None]}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.0.252'
port = 31654

s.bind((host, port))
s.listen(10)
print(f'server on {host} listening to {port}')


def new_conection(clientsocket, addr):

    while True:

        try:
            data = clientsocket.recv(1024)
            print(data)
            if data:
                recv = pickle.loads(data)
                print(f'{recv} i have got this data :O.')
                operation = recv[0]
                data = recv[1]

                if operation == 'get':
                    if data in games:
                        data = pickle.dumps((games[data]))
                    else:
                        data = pickle.dumps((None))
                    clientsocket.send(data)
                    print(f'i have sent back {data}')

                if operation == 'update':
                    games[data[0]][data[1]] = data[2]
                    print('games', games)

                if operation == 'delete':
                    games.pop(data, None)
                    print('games', games)

                if operation == 'add':
                    games[data] = [1, False, [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                    print('games', games)

        except Exception as e:
            print('ERROR', e)
            games.pop(lobby)
            break


while True:
    c, addr = s.accept()
    t = threading.Thread(target=new_conection, args=(c, addr))
    t.start()
