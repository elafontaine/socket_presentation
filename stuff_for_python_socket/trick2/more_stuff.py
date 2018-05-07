import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 15000))
server_socket.listen(5)

client_socket.connect(("localhost", 15000))  # We're connecting the client socket to the Server Socket.

connection_socket, addr_info = server_socket.accept()

client_socket.send(b"test!1,2,3,test!")
received_bytes = connection_socket.recv(1000)  # this is the number of bytes to get at most!
print(received_bytes)

server_socket.close()
