import config as cfg
import socket
import pickle
import random as rnd
import string as st
import threading
import time 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((cfg.server, cfg.port))
    print(f'connected to {cfg.server}')

except Exception as e:
    print(e)


# sends get function, recieves gamelobby's data
def get_data():
    while True:
        time.sleep(1)
        data = pickle.dumps(('get', cfg.lobby_id))
        s.send(data)
        print('waiting for response from server!!!!')
        recv = pickle.loads(s.recv(1024))
        print(f'{recv} recieved')
        cfg.game_data = recv
        
def check_data(game_lobby):

    data = pickle.dumps(('get', cfg.lobby_id))
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
    t = th.Thread(target=get_data)
    t.start()

def lobby_code():
    code = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))
    print(code)
    if get_data(code):
        print(code, 'found')
        lobby_code()
    else:
        print('valid lobby!!')
        return code
