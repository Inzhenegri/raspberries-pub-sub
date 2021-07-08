import zmq


class REP:
    def __init__(self, port, data):
        self.port = port
        self.data = data
        self.socket = None

    def bind(self):
        self.socket = zmq.Context().socket(socket_type=zmq.REP)
        self.socket.bind(addr=f'tcp://*:{self.port}')

    def receive(self):
        return self.socket.recv_pyobj()

    def send(self):
        self.socket.send_pyobj(obj=self.data)
        

rep = REP(port=5555, data={'message': 'from raspberry'})
rep.bind()

while True:
    data = rep.receive()
    print(data)

    rep.send()
