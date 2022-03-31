import config as cfg
import socket
import pickle
import random as rnd
import string as st
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port, server = 31654, "141.147.118.101"


def connect_server(game_lobby):
    try:
        print('attemptiong connection to server')
        s.connect((server, port))

    except Exception as e:
        print(e)


def get_data():

    while True:
        data = pickle.dumps(('get', cfg.lobby_id))
        s.send(data)
        data = pickle.loads(s.recv(1024))
        print(data)
        cfg.game_data = data
        time.sleep(1)


def check_data(game_lobby):

    data = pickle.dumps(('get', game_lobby))
    s.send(data)
    recv = pickle.loads(s.recv(1024))
    if recv:
        return True


def update_lobby(lobby_id, index, value):
    data = pickle.dumps(('update', (lobby_id, index, value)))
    s.send(data)
    print(f'{pickle.loads(data)[1]} updated')


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
    return code
