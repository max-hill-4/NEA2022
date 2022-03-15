import socket

class Network():
    def __init__(self):
        self.conn = None
        self.port = 5555
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None
    def build_server(self):
        self.s.bind(('', self.port))
        self.s.listen(2)
        print(f'Server built {self.port}')

    def connection_attempt(self):

        try:
            print('making attempt')
            self.connection, self.address = self.s.accept()
            print(f"Connection from: {self.address[0]}")
        except:
            print('the socket has been closed')

    def close(self):
        self.s.close()
