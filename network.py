import socket

class Network():

    def __init__(self):
        self.conn = None
        self.port = 5555
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def build_server(self):
        self.s.bind(('', self.port))
        self.s.listen(2)
        print(f'Server built {self.port}')

    def connection_attempt(self,temp):
        self.conn, self.addr = self.s.accept()
        print(f"Connection from: {self.addr[0]}")

    def connected(self):
        if self.conn:
            return True
