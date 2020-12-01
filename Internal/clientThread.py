#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
from Internal import processClientData
# from Internal import pinkServer
from Internal import exceptions
from Internal import processServerData
import threading

# from typing import List

class clientThread(threading.Thread):
    
    def __init__(self, inStream, address):
            threading.Thread.__init__(self)
            self.csocket = address
            self.inStream = inStream
            self.chunk
            self.data
            self.flag
            print("New connection added: ", inStream)
    
    #put processClientData.diagnose(data, inStream)
    def clientData(self, data, inStream):
        processClientData(data, inStream)
        return

    def getData(self):
        self.data = ''
        self.flag = False
        while True:
            self.chunk = self.inStream.recv(65536)
            self.data += self.chunk.decode("utf8")
            if "myapp".encode('utf-8') in self.chunk:
                self.flag = True
                self.data = ""
                self.inStream.send(bytes(1))
                self.chunk = self.inStream.recv(65536)
                self.data += chunk.decode("utf-8")
            if not self.data:
                print('Bye')
                break
            if "/Dataset".encode('utf-8') in self.chunk:
                break
        return self.data

    def serverData(self, data, inStream):
        processServerData(data, self.inStream)
        return

    def run(self):
        getData()
        if self.flag == True:
            clientData(self.data, self.inStream)
        else: 
            serverData(self.data, self.inStream)
        print("Client d/c'ed")
        return


	# def __init__(self):
	# 	self.___data : str = None
	# 	self.___csocket : socket = None
	# 	self.___inStream : socket = None
	# 	self.___chunk : bytes = None
	# 	self._unnamed_processClientData_ : processClientData = None
	# 	self._unnamed_pinkServer_ : pinkServer = None
	# 	self._unnamed_exceptions_ : exceptions = None
	# 	self._unnamed_processServerData_ : processServerData = None
	# 	self._unnamed_socket_ : socket = None