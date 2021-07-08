import zmq


socket = zmq.Context().socket(socket_type=zmq.REP)
socket.bind(addr='tcp://*:5555')

while True:
    message = socket.recv_pyobj()
    print(message)
    socket.send_pyobj(obj={'message': 'from raspberry'})
