import zmq


class SUB:
    def __init__(self, addr, port):
        self.socket = zmq.Context().socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')
        self.addr = addr
        self.port = port
    
    def connect(self):
        self.socket.connect(addr=f'tcp://{self.addr}:{self.port}')

    def receive(self):
        obj = self.socket.recv_pyobj()
        return obj


sub = SUB(addr='192.168.11.1', port=5555)
sub.connect()

while True:
    obj = sub.receive()
    print(obj)
