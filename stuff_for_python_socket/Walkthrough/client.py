import socket

client_socket = socket.socket()

client_socket.connect(("localhost",15000)) # blocking call, if it's to succeed

client_socket.send(b"those are the bytes you're looking for!")

client_socket.close()