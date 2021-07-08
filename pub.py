import zmq


class PUB:
    def __init__(self, port, reply_addr, reply_port):
        self.socket = zmq.Context().socket(socket_type=zmq.PUB)
        self.port = port

        self.reply_socket = None
        self.reply_addr = reply_addr
        self.reply_port = reply_port
    
    def connect(self):
        self.socket.bind(addr=f'tcp://*:{self.port}')

    def send(self, data):
        self.socket.send_pyobj(obj=data)

    def create_sub_another_raspberry(self):
        self.reply_socket = zmq.Context().socket(socket_type=zmq.SUB)
        self.reply_socket.connect(addr=f'tcp://{self.reply_addr}:{self.reply_port}')

    def receive_another_raspberry(self):
        received = self.reply_socket.recv_pyobj()
        return received


pub = PUB(port=5555, reply_addr='192.168.11.159', reply_port=5556)
pub.connect()
pub.create_sub_another_raspberry()

while True:
    messagedata = {'': None}
    pub.send(data=messagedata)
    print('Sent')

    data = pub.receive_another_raspberry()
    print(data)
