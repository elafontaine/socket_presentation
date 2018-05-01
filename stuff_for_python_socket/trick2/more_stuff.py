import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 15000))# we're going to reserve this port to start the server

# Do we see the socket on LISTEN yet? What about file descriptor?

server_socket.listen(5) # max_number of concurent connection

# Do we see the socket on LISTEN yet?

client_socket.connect(("localhost", 15000))  # We're connecting the client socket to the Server Socket.

# at this point, the client is connected, but the server still doesn't know about it.
# What does the OS tell us ; - about File descriptor? - about the netstat output?

connection_socket, addr_info = server_socket.accept()

# now the server knows, mouhahaha
# how many file descriptor de we have now?

client_socket.send(b"test!1,2,3,test!")
received_bytes = connection_socket.recv(1000)  # this is the number of bytes to get at most!
print(received_bytes)

server_socket.close()

# what happened now?

# Why do we still have 2 file descriptor?!?!?!?!?

# the socket API predict that you might want to update the server socket for changing configurations


if __name__ == '__main__':
    print("{file} is main".format(file=__file__))
else:
    print("{file} is loaded".format(file=__file__))
