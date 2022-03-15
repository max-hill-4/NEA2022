import socket


class Build_Server():

    def __init__(self):
        self.conn = None
        self.port = 5555
        self.connection = None
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', self.port))
        self.s.listen(2)
        print(f'Server built on port: {self.port}.')

    def connection_attempt(self):
        try:
            self.connection, self.address = self.s.accept()
            print(f"Connection from: {self.address[0]}")
        except Exception as e:
            print(f'{e} so socket has been closed.')

    def close(self):
        self.s.close()
