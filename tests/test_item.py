import unittest
from models import Item

class TestItem(unittest.TestCase):
    def test_update_quantity(self):
        item = Item(1, 'Laptop', 1000, 5)
        item.update_quantity(10)
        self.assertEqual(item.quantity, 10)

if __name__ == '__main__':
    unittest.main()
