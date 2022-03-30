import config as cfg
import socket
import pickle
import random as rnd
import string as st
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port, server = 5555, "141.147.118.101"

def connect_server(game_lobby)
    try:
        s.connect((server, port))
        print(f'connected to {server}')
        s.send(game_lobby)

    except Exception as e:
        print(e)


def get_data():
    while True:
        data = pickle.dumps(('get', cfg.lobby_id))
        s.send(data)
        data = pickle.loads(s.recv(1024))
        print(f'{cfg.game_data} recieved')
        cfg.game_data = data
        time.sleep(1)


def check_data(game_lobby):

    data = pickle.dumps(('get', game_lobby))
    s.send(data)
    print('waiting for response from server!!!!')
    recv = pickle.loads(s.recv(1024))
    print(f'{recv} recieved')
    if recv:
        return True


def update_lobby(lobby_id, index, value):
    data = pickle.dumps(('update', (lobby_id, index, value)))
    s.send(data)
    print(f'{pickle.loads(data)[1]} has been sent')


def del_lobby(lobby_id):
    data = pickle.dumps(('delete', lobby_id))
    s.send(data)
    print(f'{pickle.loads(data)[1]} has been deleted')


def create_lobby(lobby_id):
    data = pickle.dumps(('add', lobby_id))
    s.send(data)
    print(f'{pickle.loads(data)[1]} has been added')


def lobby_code():
    code = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))
    print(code)
    if check_data(code):
        print(code, 'found')
        lobby_code()
    else:
        print('valid lobby!!')
        return code
