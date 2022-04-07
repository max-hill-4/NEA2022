import config as cfg
import socket
import pickle
import random as rnd
import string as st
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port, server = 31654, "nidalee.maxh.cc"


def connect_server():
    try:
        s.connect((server, port))

    except Exception as e:
        print(e)


def get_data():

    while cfg.get_data is True:
        # busywait loop and not asyncrnous!!
        print("")
        # print('i have started the get thread omg')
        try: 
            data = pickle.dumps(('get', cfg.lobby_id))
            s.send(data)
            data = pickle.loads(s.recv(1024))
            cfg.game_data = data
            time.sleep(1)
            print(f' i got {data}')
        except Exception as e:
            print(e)
        
    print('get data is false')

    
def check_data(game_lobby):

    data = pickle.dumps(('get', game_lobby))
    s.send(data)
    recv = pickle.loads(s.recv(1024))
    if recv:
        return True


def close():
    s.close()


def update_lobby(index, value):
    data = pickle.dumps(('update', (cfg.lobby_id, index, value)))
    s.send(data)
    print(f'{pickle.loads(data)[1]} updated')


def create_lobby():
    lobby_id = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))
    cfg.lobby_id = lobby_id
    # need a check for if code exists here.
    data = pickle.dumps(('add', lobby_id))
    s.send(data)


def lobby_code():
    code = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))
    return code
