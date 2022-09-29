#! /usr/bin/python

import sys
import time
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

# Server is designed to accept only one client connection and shutdown
connectionSocket, addr = serverSocket.accept()
print(connectionSocket.getpeername())
connectionSocket.setblocking(False)

while True:
	try:
        	sentence = connectionSocket.recv(1024)
	except OSError as e:
		err = e.args[0]
		if err == 11 or err == 35 or err == 11002 or err == 10035:
			# No data is available
			time.sleep(0.5)
			continue
		else:
            		# a "real" error occurred
            		print(e)
            		sys.exit(1)
	else:
		# if data is recieved do something

		# handle end of data
		if sentence.decode() == '':
			break

		# write your code here
		print(sentence.decode())
