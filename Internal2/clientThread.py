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
            data += chunk.decode("utf-8")
            if not data:
                print('Bye')
                break
            if "/Dataset".encode('utf-8') in chunk:
                break
        return data

    def serverData(data, inStream):
        processServerData(data, inStream)
        return

    def run(self):
        data = self.getData()
        processServerData.diagnose(data, self.inStream)
        print("Client d/c'ed")
        return