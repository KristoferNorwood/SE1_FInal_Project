import socket, time

socket = socket.socket()
socket.connect(("localhost", 54610))
file = open(r"schema.xml", "rb")
stream = file.read(65536)
i = 0
while stream:
    socket.send(stream)
    ans = input('\nPress any button to exit: ')
    break

socket.close()