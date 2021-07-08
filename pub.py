import zmq


class PUB:
    def __init__(self, port):
        self.socket = zmq.Context().socket(socket_type=zmq.PUB)
        self.port = port
    
    def connect(self):
        self.socket.bind(addr=f'tcp://*:{self.port}')

    def send(self, data):
        self.socket.send_pyobj(obj=data)


pub = PUB(port=5555)
pub.connect()

while True:
    messagedata = {'': None}
    pub.send(data=messagedata)
    print('sending...')
