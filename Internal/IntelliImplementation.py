#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List

class IntelliImplementation(object):
	"""@Interface"""
	__metaclass__ = ABCMeta
	@abstractmethod
	def diagnose(self, aData : str) -> int:
		pass

