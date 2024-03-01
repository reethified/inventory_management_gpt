import unittest
from models import Admin, Item

class TestAdmin(unittest.TestCase):
    def test_restock_item(self):
        admin = Admin("John")
        item = Item(1, 'Laptop', 1000, 5)
        admin.restock_item(item, 10)
        self.assertEqual(item.quantity, 15)

    def test_update_item_price(self):
        admin = Admin("John")
        item = Item(1, 'Laptop', 1000, 5)
        admin.update_item_price(item, 1200)
        self.assertEqual(item.price, 1200)

if __name__ == '__main__':
    unittest.main()
