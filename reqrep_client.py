import zmq


class REQ:
    def __init__(self, addr, port, data=None):
        self.addr = addr
        self.port = port
        self.data = data

        self.socket = None

    def connect(self):
        self.socket = zmq.Context().socket(zmq.REQ)
        self.socket.connect(addr=f'tcp://{self.addr}:{self.port}')

    def send(self):
        if self.socket is not None:
            self.socket.send_pyobj(obj=self.data)
    
    def receive(self):
        if self.socket is not None:
            self.socket.recv_pyobj()

req = REQ(addr='192.168.11.1', port=5555, data={'message': 'from laptop'})

req.connect()

while True:
    req.send()

    message = req.receive()
    # print(message)
