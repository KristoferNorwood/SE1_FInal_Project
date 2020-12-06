#!/usr/bin/python
import socket
from clientThread import clientThreader 
import threading
import logging
from typing import List

def startServer():
	myLogger = logging.getLogger('myLogger')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = ('192.168.0.43', 7123)
	s.bind(server_address)
	myLogger.info('Server Started')
	print('Socket is listening...\n')
	#Every connection starts a new thread and the server continues to listen for new connections after each thread is started
	while True:
		s.listen(5)
		inbound_stream, address = s.accept()
		myLogger.info('New request from ' + address[0] + 'idk if this will print continuously or not')
		inbound_stream.settimeout(15)
		newthread = clientThreader(inbound_stream, address)
		newthread.start()
		newthread.join()
	myLogger.info('Server shutdown from server outside while')
	return


		

