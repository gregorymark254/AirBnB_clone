import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_cmd.onecmd('quit'))
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_EOF_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_cmd.onecmd('EOF'))
            self.assertEqual(mock_stdout.getvalue(), "\n")

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.emptyline()
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_help_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd('help')
            self.assertIn("List available commands", mock_stdout.getvalue())

    def test_unknown_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd('unknown_cmd')
            self.assertIn("** Unknown command:", mock_stdout.getvalue())

    def test_custom_prompt(self):
        self.assertEqual(self.hbnb_cmd.prompt, "(hbnb) ")

    def test_cmdloop_exit(self):
        def test_cmdloop_exit(self):
            with patch('builtins.input', side_effect=['quit']):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    HBNBCommand().cmdloop()
                    self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")


if __name__ == '__main__':
    unittest.main()
