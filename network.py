import config as cfg
import socket
import pickle
import string
import random as rnd


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
    return recv


def check_data(data):
    games = get_data()
    for i, v in enumerate(games):
        if v[0] == data:
            return True


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


def create_gamelobby():
    id = ''.join(rnd.choices(string.ascii_uppercase + string.digits, k=4))

    if check_data():
        create_gamelobby()
    else:
        return id
