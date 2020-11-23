import socket
import threading
import io, time
from lxml import etree as et
from app import PopUpMessage

ppm = PopUpMessage()

def processdata(data): #The data example is the actual xml schema
    root = et.fromstring(data) #once we get the root, we can iterate over the elements in the tree
    # for e in root:#.findall("Patient"): 
        # e.text = '24' #For every element in the root, we can assign values however we would like. 
        #We can tell which element is which by using e.tag like below. 
    # for e in root:#.findall("Patient"):
    #     print(e.tag, e.text) #e.tag is the actual tagname of the xml element, and e.text is the actual value stored by that element
    # for e in root: #Every element in root is every patient. 
    #     print(e.text)
    for e in root:
        for c in e: #Every C in E are the attributes of each patient. 
            print(c.tag, c.text)

    # pass


class ClientThread(threading.Thread):
    def __init__(self, inStream, clientAdd):
        threading.Thread.__init__(self)
        self.csocket = clientAdd
        self.inStream = inStream
        print("New connection added: ", inStream)

    def run(self):
        print("connection from : ", self.csocket)
        data = ""
        while True:

            # parser = ET.XMLParser(encoding="utf-8")
            chunk = self.inStream.recv(65536)
            data += chunk.decode("utf8")
            # print(data)

            if not data:
                print('Bye')
                break
            if "\n".encode('utf-8') in chunk:
                break
        processdata(data) #We can send the data to be processed however we need by defining the function above. 
        ppm.popupMsg("Benign")
        print("Client d/c'ed")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('192.168.1.69', 7123)
s.bind(server_address)

print('Socket is listening...\n')
#Every connection starts a new thread and the server continues to listen for new connections after each thread is started
while True:
    flag = False
    s.listen(1)
    inbound_stream, address = s.accept()
    newthread = ClientThread(inbound_stream, address)
    newthread.start()
    newthread.join()
    # s.close()

# s.close() # TODO NOT REACHABLE
