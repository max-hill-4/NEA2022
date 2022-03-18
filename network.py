import socket
import config as cfg


def build_server():
    global s 
    conn = None
    port = 5555
    connection = None
    cfg.socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cfg.socket_object.bind(('', cfg.port))
    cfg.socket_object.listen(2)
    print(f'Server built on port: {port}.')
    print(f'socket obj: {s}')

def connection_attempt():
    global s 
    try:
        connection, address = cfg.socket_object.accept()
        print(f"Connection from: {address[0]}")
    except Exception as e:
        print(f'{e} so socket has been closed.')

def close(self):
    cfg.socket_object.close()
