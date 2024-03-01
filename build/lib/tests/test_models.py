# File: test_models.py

import unittest
from models import Stock, Item, Admin, Transaction

class TestItem(unittest.TestCase):
    def test_update_quantity(self):
        item = Item("Test", 10, 5)
        item.update_quantity(8)
        self.assertEqual(item.quantity, 8)

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock()
        self.item = Item("Test", 10, 5)

    def test_add_item(self):
        self.stock.add_item(self.item)
        self.assertIn("Test", self.stock.items)

    def test_remove_item(self):
        self.stock.add_item(self.item)
        self.stock.remove_item("Test")
        self.assertNotIn("Test", self.stock.items)

    # Add more test cases for other functions in Stock class

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.stock = Stock()
        self.admin = Admin("admin", "password")
        self.item = Item("Test", 10, 5)

    def test_add_stock(self):
        self.admin.add_stock(self.stock, self.item)
        self.assertIn("Test", self.stock.items)

    # Add more test cases for other functions in Admin class

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.item = Item("Test", 10, 5)
        self.transaction = Transaction()

    def test_make_sale(self):
        self.transaction.make_sale(self.item, 3)
        self.assertEqual(self.item.quantity, 2)

    # Add more test cases for other functions in Transaction class

if __name__ == "__main__":
    unittest.main()
