import socket
import threading
import logging
import io, time
from lxml import etree as et
from lib2to3.fixer_util import String
import random

friendServers = [["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123], ["98.168.143.109", 7123]]

def getVerdict(diagArray):
    vote = 0
    vote1 = 0
    for num in diagArray:
        if num == 2:
            vote += 1
        else:
            vote1 += 1
    if vote1 > vote:
        return True
    else:
        return False
    

def getFriendDiagnosis(data):
    diagnosis = ""
    root = et.fromstring(data) 
    for patient in root:
        diagnosis = patient.find('class').text
    diag = int(diagnosis)
    return diag

def intelligentDiagnosisModel(data):
    #Diagnosis model function
    root = et.fromstring(data) # The Dataset
    for patient in root: # Patients in Dataset
        print(patient.tag + " " + patient.get("id"))
        for attributes in patient: # Patient cancer attributes
            print(attributes.tag + " " + attributes.text) 
    diagnosis = random.randrange(2, 6, 2)
    print("\nDiagnosing patient \n")
    return diagnosis

def processServerData(data, inStream):
    print("Printing data received from the other Client/Servers : \n")
    root = et.fromstring(data) 
    diagnosis = intelligentDiagnosisModel(data)
    for patient in root:
        patient.find('class').text = str(diagnosis)
    myRoot = et.tostring(root)
    inStream.send(bytes(myRoot))
    inStream.close()
    

def processClientData(data, inStream): 
    root = et.fromstring(data) 
    i = 0
    j = 0
    diagnosis = []
    myRoot = et.tostring(root)
    for i in range(12):
        s = socket.socket()
        s.settimeout(30)
        s.connect((friendServers[i][j],friendServers[i][j+1]))
        while True:
            s.send(bytes(myRoot))
            incomingVote = s.recv(65536)
            friendData = incomingVote.decode("utf8")
            diagnosis[i] = getFriendDiagnosis(friendData)
            s.close()
            break
    myDiag = intelligentDiagnosisModel(data)
    diagnosis[12] = myDiag
    verdict = getVerdict(diagnosis)
    if verdict:
        myDiag = 2
    else:
        myDiag = 4
    for patient in root:
        patient.find('class').text = str(myDiag)
    myRoot = et.tostring(root)
    inStream.send(bytes(myRoot))
    inStream.close()
    
class ClientThread(threading.Thread):
    def __init__(self, inStream, address):
        threading.Thread.__init__(self)
        self.csocket = address
        self.inStream = inStream
        print("New connection added: ", inStream)

    def run(self):
        print("connection from : ", self.csocket)
        data = ""
        flag = False
        while True:
            
            chunk = self.inStream.recv(65536)
            data += chunk.decode("utf8")
            if "myapp".encode('utf-8') in chunk:
                flag = True
                data = ""
                self.inStream.send(bytes(1))
                chunk = self.inStream.recv(65536)
                data += chunk.decode("utf-8")
            if not data:
                print('Bye')
                break
            if "/Dataset".encode('utf-8') in chunk:
                break
        if flag == True:
            processClientData(data, self.inStream)
        else: 
            processServerData(data, self.inStream)
        print("Client d/c'ed")
        return
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('192.168.0.43', 7123)
s.bind(server_address)

print('Socket is listening...\n')
#Every connection starts a new thread and the server continues to listen for new connections after each thread is started
while True:
    flag = False
    s.listen(5)
    inbound_stream, address = s.accept()
    inbound_stream.settimeout(15)
    newthread = ClientThread(inbound_stream, address)
    newthread.start()
    newthread.join()
    
