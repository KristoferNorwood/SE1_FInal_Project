#!/usr/bin/python
import socket
import processClientData
import processServerData
import threading
from typing import List
import logging

class clientThreader(threading.Thread):

    def __init__(self, inStream, address):
        threading.Thread.__init__(self)
        self.csocket = address
        self.inStream = inStream
        print("New connection added: ", inStream)
        self.myLogger = logging.getLogger('myLogger')

    #put processClientData.diagnose(data, inStream)
    def checkData(self, data):
    #validate the data
        i = 0
        flag = True
        file = open(r"schema.xml", "rb")
        mydata = file.read(65536)
        myroot = et.fromstring(mydata)
        root = et.fromstring(data) # The Dataset
        if myroot.tag == root.tag:
            mynothingvariable = "Don't use this"
        else:
            flag = False
        for i in range(10):
            if root[0][i].text == myroot[0][i].text:
                continue
            else:
                flag = False
                break
        for patient in root:
            if int(patient.find('class').text) == 2 or int(patient.find('class').text) == 4:
                break
            else:
                flag = False
        return flag

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
        if (not(self.checkData(data))):
            self.myLogger.error('incorrect xml schema')
        
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