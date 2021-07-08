import zmq


class SUB:
    def __init__(self, addr, port, reply_port, reply_data):
        self.socket = zmq.Context().socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')
        self.addr = addr
        self.port = port

        self.reply_port = reply_port
        self.reply_data = reply_data

        self.reply_socket = None
    
    def connect(self):
        self.socket.connect(addr=f'tcp://{self.addr}:{self.port}')

    def receive(self):
        obj = self.socket.recv_pyobj()
        return obj

    def reply_connect(self):
        self.reply_socket = zmq.Context().socket(socket_type=zmq.PUB)
        self.reply_socket.bind(addr=f'tcp://*:{self.reply_port}')

    def reply_send(self):
        if self.reply_socket is not None:
            self.reply_socket.send_pyobj(self.reply_data)
        else:
            raise Exception('self.reply_scoket is None')


sub = SUB(addr='192.168.11.1', port=5555, reply_port=5556, reply_data={'message': 'OK'})
sub.connect()
sub.reply_connect()

while True:
    obj = sub.receive()
    print(obj)
