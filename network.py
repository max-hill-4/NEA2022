import config as cfg
import socket
import pickle
import string as st
import random as rnd


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((cfg.server, cfg.port))
    print(f'connected to {cfg.server}')

except Exception:
    print('server not online!')


def get_data(lobby_id):
    data = pickle.dumps(lobby_id)
    s.send(data)
    recv = pickle.loads(s.recv(1024))
    return recv


def check_data(lobby_id):

    games = get_data(lobby_id)
    if games:
        return True
    else:
        print(f'{lobby_id} not found')


def write_data(new_data):
    data = pickle.dumps('write')
    s.send(data)
    data = pickle.dumps((new_data))
    s.send(data)
    print(f'{pickle.loads(data)} has been sent')


def del_data(lobby_id):
    data = pickle.dumps('delete')
    s.send(data)
    data = pickle.dumps(lobby_id)
    s.send(data)
    print(f'{pickle.loads(data)} has been deleted')


def create_gamelobby():
    cfg.lobby = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))

    if check_data(id):
        write_data(id)
        return id
    else:
        create_gamelobby()
