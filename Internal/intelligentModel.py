#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Internal import processClientData
from Internal import processServerData
from typing import List

class intelligentModel(object):
	__metaclass__ = ABCMeta
	@classmethod
	def diagnose(self, aData : str) -> int:
		pass

	@classmethod
	def setImp(self, aIntelliModel : intelliImplementation) -> None:
		self.___imp = aIntelliModel

	@classmethod
	def __init__(self):
		self.___imp : intelliImplementation = None
		self._unnamed_processClientData_ : processClientData = None
		self._unnamed_processServerData_ : processServerData = None

