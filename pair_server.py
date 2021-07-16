import zmq
import time
import threading

def sock_1():
    while True:
        socket_1.send_pyobj({'message': 'from raspberry_master'})
        ok = socket_1.recv_string()

def sock_2():
    while True:
        msg = socket_2.recv_pyobj()
        socket_2.send_string('OK')
        print(msg)

port_1 = "5556"
port_2 = "5557"

socket_1 = zmq.Context().socket(zmq.PAIR)
socket_1.bind(f'tcp://*:{port_1}')
print('done_1')

socket_2 = zmq.Context().socket(zmq.PAIR)
socket_2.bind(f'tcp://*:{port_2}')
print('done_2')

socket_thread_1 = threading.Thread(target=sock_1, args=())
socket_thread_2 = threading.Thread(target=sock_2, args=())

socket_thread_1.start()
socket_thread_2.start()

while True:
    pass