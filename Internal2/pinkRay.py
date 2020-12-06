#!/usr/bin/python
import app
import pinkServer
import logging
from typing import List
import threading
from tkinter import Tk, StringVar, BOTH, W, E, ttk

def get_logger(name):
    log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        filename='PinkRayLog.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger(name).addHandler(console)
    return logging.getLogger(name)

myLogger = get_logger('myLogger')
myLogger.info('Pink Ray Ready to Serve')
newThread2 = threading.Thread(target=pinkServer.startServer, args=())
newThread = threading.Thread(target=app.mainer, args=())
newThread.start()
newThread2.start()
newThread.join()
newThread2.join()
