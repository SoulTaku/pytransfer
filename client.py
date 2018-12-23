#!/usr/bin/python
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((input('IP > '), 420))
files = pickle.loads(s.recv(1024))

for f in files:
	print(f)

name = input('file > ')

s.send(name.encode())

data = pickle.loads(s.recv(4096))
open(name, 'w').write(data)

