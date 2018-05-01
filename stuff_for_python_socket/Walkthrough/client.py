import socket

client_socket = socket.socket()

client_socket.connect(("localhost",15000))

client_socket.send(b"those are the bytes you're looking for!")

client_socket.close()

if __name__ == '__main__':
    print("{file} is main".format(file=__file__))
else:
    print("{file} is loaded".format(file=__file__))