#!/usr/bin/python
import guiApplication
import pinkServer
import logging
from typing import List


pinkServer.startServer
guiApplication.main()

def get_logger(name):
    log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        filename='Team3Log.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger(name).addHandler(console)
    return logging.getLogger(name)

# class pinkRay(object):
# 	# def startSystem(self) -> None:
# 		pass

# 	# def __init__(self):
# 		self.___gui : guiApplication = None
# 		self.___server : pinkServer = None
# 		self.___pinkLogger : logging = None
# 		self._unnamed_logging_ : logging = None
# 		self._unnamed_guiApplication_ : guiApplication = None
# 		self._unnamed_pinkServer_ : pinkServer = None

