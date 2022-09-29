#! /usr/bin/python

from socket import *
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('',12001))
clientSocket.connect((serverName,serverPort))

num=0
num_max = 20; # modify for varying the numbers to be sent
send_delay = 1;

while num < num_max:
	num=num+1
	print(num)
	clientSocket.send(str(num).encode())
	time.sleep(send_delay) # vary delay here

clientSocket.close()
print('Connection Closed')
