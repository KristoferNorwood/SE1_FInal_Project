#!/usr/bin/python
import socket
import intelligentModel
from typing import List
from lxml import etree as et
import logging


def diagnose(data, inStream, address):
	#replace with intelligentModel.diagnose or 
	#whatever the class above the intelliImplementor is
	# diagnosis = intelligentModel(data)
	myLogger = logging.getLogger('myLogger')
	print("Printing data received from the other Client/Servers : \n")
	root = et.fromstring(data) 
	diagnosis = intelligentModel.diagnose(data)
	for patient in root:
		patient.find('class').text = str(diagnosis)
	myRoot = et.tostring(root)
	if (diagnosis == 2):
		myLogger.info('response to ' + address[0] + ' is patient diagnosis is non-cancerous')
	else:
		myLogger.info('response to ' + address[0] + ' is patient diagnosis is cancerous')
	inStream.send(bytes(myRoot))
	inStream.close()
	return
