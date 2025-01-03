from unittest import TestCase, main
from py_style.models import Table

class TestTable(TestCase):

    def setUp(self):
        self.table = Table(columns=3)

    def test_add_row(self):
        self.table.add_row(1, 2, 3)
        self.assertEqual(self.table.get_row(0), [1, 2, 3])

    def test_add_column(self):
        self.table.add_row(1, 2, 3)
        self.table.add_column(placeholder=0)
        self.assertEqual(self.table.get_row(0), [1, 2, 3, 0])

    def test_del_row(self):
        self.table.add_row(1, 2, 3)
        self.table.del_row(0)
        self.assertEqual(len(self.table.table), 0)

    def test_del_column(self):
        self.table.add_row(1, 2, 3)
        self.table.del_column(1)
        self.assertEqual(self.table.get_row(0), [1, 3])

    def test_get_set_column(self):
        self.table.add_row(1, 2, 3)
        self.assertEqual(self.table.get_column(0, 1), 2)
        self.table.set_column(10, 0, 1)
        self.assertEqual(self.table.get_column(0, 1), 10)

    def test_get_table_string(self):
        self.table.add_row(1, 2, 3)
        table_str = self.table.get_table()
        self.assertIn("| 1 | 2 | 3 |", table_str)
    
if __name__ == "__main__":
    main()
