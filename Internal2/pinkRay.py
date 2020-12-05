#!/usr/bin/python
import guiApplication
import pinkServer
import logging
import pinkServer
from typing import List
import threading

class clientThreader(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        myLogger = logging.getLogger('myLogger')
        # myLogger.info('Server Started')
        pinkServer.startServer
        return
