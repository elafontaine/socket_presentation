import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 15000))

server_socket.listen(5) # 5 max number of connection

connection_socket, addr_info = server_socket.accept() # blocking call!

print(connection_socket.recv(4096)) # blocking call!

server_socket.close()

connection_socket.close()
