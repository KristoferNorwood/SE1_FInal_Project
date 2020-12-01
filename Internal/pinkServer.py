#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
# import clientThread.py
from Internal import clientThread
from Internal import threading
from Internal import exceptions
from Internal import logging
from typing import List

class pinkServer(object):
	def startServer(self) -> None:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_address = ('192.168.0.43', 7123)
		s.bind(server_address)

		print('Socket is listening...\n')
		#Every connection starts a new thread and the server continues to listen for new connections after each thread is started
		while True:
			flag = False
			s.listen(5)
			inbound_stream, address = s.accept()
			inbound_stream.settimeout(15)
			newthread = clientThread(inbound_stream, address)
			newthread.start()
			newthread.join()
		

	# def processData(self, aThread : ClientThread, aInStream : socket, aAddress : socket) -> None:
	# 	pass

	def __init__(self):
		self.___s : socket = None
		self.___serverAddress : tuple = None
		self.___newThread : clientThread = None
		self.___inbound_stream : socket = None
		self.___address : socket = None
		self._unnamed_pinkRay_ : pinkRay = None
		self._unnamed_threading_ : threading = None
		self._unnamed_exceptions_ : exceptions = None
		self._unnamed_logging_ : logging = None
		self._unnamed_clientThread_ : clientThread = None
		self.startServer()
		

