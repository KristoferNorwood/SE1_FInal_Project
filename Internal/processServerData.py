#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
from Internal import intelligentModel
from typing import List
from lxml import etree as et

class processServerData(object):
	
	def __init__(self, data, inStream):
		self.data = data
		self.inStream = inStream
		self.intelligentModel: intelligentModel
		self.diagnose()

	def diagnose(self):
		#replace with intelligentModel.diagnose or 
		#whatever the class above the intelliImplementor is
		# diagnosis = intelligentModel(data)
		print("Printing data received from the other Client/Servers : \n")
		root = et.fromstring(data) 
		diagnosis = intelligentModel.diagnose(data)
		for patient in root:
			patient.find('class').text = str(diagnosis)
		myRoot = et.tostring(root)
		inStream.send(bytes(myRoot))
		inStream.close()
		return
