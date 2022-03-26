import config as cfg
import socket
import pickle


def connect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((cfg.server, cfg.port))
        print(f'connected to {cfg.server}')

    except Exception:
        print('server not online!')

def get_data():
    data = pickle.dumps('get')
    s.send(data)
    recv = pickle.loads(s.recv(1024))
    print(list(recv))


def write_data(lobby_id, P1, P2):
    data = pickle.dumps('write')
    s.send(data)
    data = pickle.dumps((lobby_id, P1, P2))
    s.send(data)
    print(f'{pickle.loads(data)} has been sent')


def del_data(lobby_id):
    data = pickle.dumps('delete')
    s.send(data)
    data = pickle.dumps(lobby_id)
    s.send(data)
    print(f'{pickle.loads(data)} has been sent')


connect()
while True:

    x = input()
    if x == 'g':
        get_data()

    if x == 'w':
        lobby_id = input('lobby_id:')
        P1 = input('P1:')
        P2 = input('P2:')

        write_data(lobby_id, P1, P2)
    if x == 'd':
        lobby_id = input('id to delete:')
        del_data(lobby_id)
