#!/usr/bin/python
import socket
import intelligentModel
from typing import List
from lxml import etree as et
import logging

def diagnose(data, inStream):
	#replace with intelligentModel.diagnose or 
	#whatever the class above the intelliImplementor is
	# diagnosis = intelligentModel(data)
	logging.getLogger('myLogger')
	print("Printing data received from the other Client/Servers : \n")
	root = et.fromstring(data) 
	diagnosis = intelligentModel.diagnose(data)
	for patient in root:
		patient.find('class').text = str(diagnosis)
	myRoot = et.tostring(root)
	logging.info(diagnosis + ' response to ')
	inStream.send(bytes(myRoot))
	inStream.close()
	return
