#!/usr/bin/python
from lxml import etree as et
from typing import List
import random

def diagnose(data):
	#Diagnosis model function
	root = et.fromstring(data) # The Dataset
	for patient in root: # Patients in Dataset
		print(patient.tag + " " + patient.get("id"))
		for attributes in patient: # Patient cancer attributes
			# print(attributes.tag + " " + attributes.text) 
	diagnosis = random.randrange(2, 6, 2)
	print("\nDiagnosing patient \n")
	return diagnosis
	# pass

