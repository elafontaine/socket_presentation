import socket

if __name__ == '__main__':
    print("{file} is main".format(file=__file__))
    client_socket = []
    server_socket = socket.socket()
    server_socket.bind(("localhost",0))
    server_socket.listen(65000)
    while (True):
        current_socket = socket.socket()
        client_socket.append(current_socket)
        current_socket.connect(server_socket.getsockname())
        connection_socket, addr_info = server_socket.accept()
        connection_socket.close()

else:
    print("{file} is loaded".format(file=__file__))