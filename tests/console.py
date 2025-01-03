from unittest import TestCase, main
from io import StringIO
from unittest.mock import patch
from py_style import Console, Theme

class TestConsole(TestCase):

    def setUp(self):
        self.console = Console("Test Console")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_title(self, mock_stdout):
        self.console.print_title()
        self.assertIn("Test Console", mock_stdout.getvalue())

    @patch("builtins.input", return_value="User input")
    def test_prompt(self, mock_input):
        result = self.console.prompt("Enter something:")
        self.assertEqual(result, "User input")

    @patch("sys.stdout", new_callable=StringIO)
    def test_write_and_log(self, mock_stdout):
        self.console.write("Test message")
        self.console.log("Log message")
        output = mock_stdout.getvalue()
        self.assertIn("Test message", output)
        self.assertIn("Log message", output)

    def test_theme_setter(self):
        new_theme = Theme(info="cyan", warning="yellow", error="red", success="green")
        self.console.theme = new_theme
        self.assertEqual(self.console.theme, new_theme)
    
if __name__ == "__main__":
    main()
