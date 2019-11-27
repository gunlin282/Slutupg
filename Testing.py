import unittest
import pickle
from Server import input_output_with_client

class testing(unittest.TestCase):



    def test_client_input(self):
        input_output = ("pasta carbonara")
        input_output = pickle.dumps(input_output)
        input_output_with_client(input_output)
        self.assertEqual(pickle.loads(input_output), "pasta carbonara")

