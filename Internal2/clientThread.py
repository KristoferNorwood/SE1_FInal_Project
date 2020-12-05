#!/usr/bin/python
import socket
import processClientData
import processServerData
import threading
from typing import List

class clientThreader(threading.Thread):
    
    def __init__(self, inStream, address):
        threading.Thread.__init__(self)
        self.csocket = address
        self.inStream = inStream
        print("New connection added: ", inStream)

    #put processClientData.diagnose(data, inStream)

    def getData(self):
        data = ''
        while True:
            chunk = self.inStream.recv(65536)
            data += self.chunk.decode("utf8")
            if not data:
                print('Bye')
                break
            if "/Dataset".encode('utf-8') in chunk:
                break
        return data

    def serverData(self, data, inStream):
        processServerData(data, inStream)
        return

    def run(self):
        data = getData()
        processServerData.diagnose(data, self.inStream)
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