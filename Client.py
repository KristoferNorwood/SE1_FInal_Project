import socket, time

socket = socket.socket()
socket.connect(('71.156.28.25', 7123))
file = open(r"schema.xml", "rb")
stream = file.read(65536)
i = 0
while stream:
    socket.send(stream)
    ans = input('\nPress any button to exit: ')
    break

socket.close()