import unittest
from socket import socket
from pickle import *
from Server import *

# starta testing server innan unittest
class testing(unittest.TestCase):

    def test_client_input(self):
        input_output = ("pasta carbonara")
        input_output = pickle.dumps(input_output)
        input_output_with_client(input_output)
        self.assertEqual(pickle.loads(input_output), "pasta carbonara")

class Test_server_connection(unittest.TestCase):

    def setUp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("127.0.0.1", 65432))

    def tearDown(self):
        self.s.close()

    def test(self):
        self.s.send("hej".encode())
        self.assertEqual(self.s.recv(1024).decode(), "hej")


if __name__ == '__main__':
    unittest.main()