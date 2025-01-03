from unittest import TestCase, main
from io import StringIO
from unittest.mock import patch
from py_style import ProgressBar

class TestProgressBar(TestCase):

    def setUp(self):
        self.progress_bar = ProgressBar(values=5, symbol="#", delay=0.1)

    @patch("time.sleep", return_value=None)
    @patch("sys.stdout", new_callable=StringIO)
    def test_run(self, mock_stdout, mock_sleep):
        self.progress_bar.run()
        self.assertEqual(mock_stdout.getvalue().count("#"), 5)

    def test_values_setter(self):
        self.progress_bar.values = 10
        self.assertEqual(self.progress_bar.values, 10)
    
if __name__ == "__main__":
    main()
