#!/usr/bin/python
import socket
import os
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 420))

print('Listening on port 420...')

s.listen(10)

while True:
	conn, addr = s.accept()
	print('Connection from {}'.format(addr))
	conn.send(pickle.dumps(os.listdir('.')))

	f = conn.recv(1024)

	data = open(f, 'r').read()
	data = pickle.dumps(data)

	conn.send(data)
	print('Data sent to {}'.format(addr))
