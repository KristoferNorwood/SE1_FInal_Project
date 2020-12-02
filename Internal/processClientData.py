#!/usr/bin/python

import socket
import intelligentModel
import clientThread
from lxml import etree as et
from typing import List

class processClientData(object):
	def __init__(self, data, inStream):
		super().__init__()
		self.data = data
		self.inStream: socket = inStream
		self.friendServers = [["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], 
    		["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], 
    		["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123], ["71.156.28.25", 7123]]
		self.diagnosis
		self.intelligentModel : intelligentModel
		self.myRoot
		self.verdict
		self.root
		self.sendDiagReq()
		self.diagnose()

	def sendDiagReq(self) -> None:
		self.root = et.fromstring(self.data) 
		i = 0
		j = 0
		self.diagnosis = []
		self.myRoot = et.tostring(root)
		# diagnosis.insert(3, 29)
		for i in range(12):
			s = socket.socket()
			s.settimeout(30)
			s.connect((friendServers[i][j],friendServers[i][j+1]))
			while True:
				s.send(bytes(myRoot))
				incomingVote = s.recv(65536)
				friendData = incomingVote.decode("utf8")
				self.diagnosis.insert(i, getFriendDiagnosis(friendData))
				s.close()
				break

	def diagnose(self):
		#change to intelligentModel.diagnose or whatever
		myDiag = intelligentModel(self.data)
		self.diagnosis.insert(12, myDiag)
		self.verdict = getVerdict()
		if verdict:
			myDiag = 2
		else:
			myDiag = 4
		for patient in self.root:
			patient.find('class').text = str(myDiag)
		self.myRoot = et.tostring(self.root)
		self.inStream.send(bytes(myRoot))
		self.inStream.close()
		return

	def getVerdict(self):
		vote = 0
		vote1 = 0
		for num in self.diagnosis:
			if num == 2:
				vote += 1
			else:
				vote1 += 1
		if vote1 > vote:
			return True
		else:
			return False
    

	def getFriendDiagnosis(self, data):
		diagnosis = ""
		root = et.fromstring(data) 
		for patient in root:
			diagnosis = patient.find('class').text
		diag = int(diagnosis)
		return diag