import config as cfg
import socket
import pickle
import random as rnd
import string as st
import time

# create socket instance
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port, server = 31654, "nidalee.maxh.cc"


def connect_server():
    # attempt connection to the server
    try:
        s.connect((server, port))
    # print the error if it doesnt work
    except Exception as e:
        print(e)


def get_data():
    # if global boolean get_data
    while cfg.get_data is True:
        # print statment updates the busywait loop to actually function
        print("")
        try: 
            data = pickle.dumps(('get', cfg.lobby_id))
            s.send(data)
            data = pickle.loads(s.recv(1024))
            cfg.game_data = data
            time.sleep(1)
            print(f' i got {data}')
        except Exception as e:
            print(e)

    
def check_data(game_lobby):
    # game_lobby = game_id
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
    # create length 4 string containing integers and characters
    lobby_id = ''.join(rnd.choices(st.ascii_uppercase + st.digits, k=4))
    cfg.lobby_id = lobby_id
    data = pickle.dumps(('add', lobby_id))
    s.send(data)
