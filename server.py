#!/usr/bin/python
import socket
import os
import threading
import pickle


def callback(conn, addr):
    conn.send(pickle.dumps(os.listdir('.')))

    f = conn.recv(1024)

    print(f'{addr[0]} requested {f.decode()}')

    data = open(f, 'rb').read()
    data = pickle.dumps(data)

    conn.send(data)

    print(f'Data sent to {addr}')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 420))

print('Listening on port 420...')

s.listen(10)

while True:
        conn, addr = s.accept()
        print('Connection from {}'.format(addr))

        t = threading.Thread(target=callback, args=(conn, addr))
        try:
            t.start()

        except Exception as e:
            print(f'Some error occured on connection {addr}')
            print(str(e))
