import socket
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.server_socket = socket.socket()
        self.server_socket.settimeout(2)
        self.server_socket.bind(('localhost', 0))
        self.server_socket.listen(10)
        self.client_socket = socket.socket()

    def tearDown(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()

    def test_we_can_connect_to_a_server_socket(self):
        expected_bytes = b"this is the expected value"

        self.client_socket.connect(self.server_socket.getsockname())
        connection_socket, _ = self.server_socket.accept()
        self.client_socket.send(expected_bytes)
        connection_socket.settimeout(2)
        actual_bytes = connection_socket.recv(1000)
        self.assertEqual(actual_bytes, expected_bytes)
        connection_socket.close()


    def test_we_can_connect_and_manage_2_connection_simultanously(self):
        pass


if __name__ == '__main__':
    unittest.main()
