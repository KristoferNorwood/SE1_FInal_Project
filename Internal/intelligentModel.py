#!/usr/bin/python
from abc import ABC, abstractmethod
from typing import List
import intelliImplementation

class intelligentModel:
	def __init__(self, data):
		self.diagnosis
		self.data = data
		self.imp = intelliImplementation(data)
		self._unnamed_processClientData_ : processClientData = None
		self._unnamed_processServerData_ : processServerData = None
	
	def diagnose(self):
		self.diagnosis = imp.diagnose()
		return self.diagnosis
	
