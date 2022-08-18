#!/usr/bin/env python3

import socket
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = '127.0.0.1'
port = 12000

sock.bind((address,port))
print("Ping server ready on port", port)

while True:
	_, client_address = sock.recvfrom(1024)

	rand = random.randint(0, 10)
	if rand < 4:
		continue

	sock.sendto("pong".encode(), client_address)

sock.close()
