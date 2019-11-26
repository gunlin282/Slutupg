import unittest
import pickle
from Server import input_output_with_client

class testing(unittest.TestCase):

    def test_client_input(self):
        input_output = input_output_with_client(self)
        input_output.add(["s", "pasta carbonara"])
        input_output = pickle.dumps(input_output)
        self.assertEqual("Varor inlagda", pickle.loads(input_output))
