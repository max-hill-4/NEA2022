import socket
import config as cfg


def build_server():
    cfg.socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cfg.socket_object.bind(('', cfg.port))
    cfg.socket_object.listen(2)
    print(f'Server built on port: {cfg.port}.')


def connection_attempt():
    try:
        cfg.connection, cfg.address = cfg.socket_object.accept()
        print(f"Connection from: {cfg.address[0]}")
    except Exception as e:
        print(f'{e} so socket has been closed.')


def close():
    cfg.socket_object.close()
