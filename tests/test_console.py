import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        # Create an instance of the HBNBCommand class and redirect stdout
        self.stdout_patch = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.stdout_patch.start()

    def tearDown(self):
        # Clean up and stop redirecting stdout
        self.stdout_patch.stop()


if __name__ == '__main__':
    unittest.main()
