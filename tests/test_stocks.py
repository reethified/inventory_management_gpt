import unittest
from models import Stock, Item

class TestStock(unittest.TestCase):
    def test_add_item(self):
        stock = Stock()
        item = Item(1, 'Laptop', 1000, 5)
        stock.add_item(item)
        self.assertEqual(len(stock.items), 1)

    def test_remove_item(self):
        stock = Stock()
        item = Item(1, 'Laptop', 1000, 5)
        stock.add_item(item)
        stock.remove_item(1)
        self.assertEqual(len(stock.items), 0)

    def test_update_item(self):
        stock = Stock()
        item = Item(1, 'Laptop', 1000, 5)
        stock.add_item(item)
        updated_item = Item(1, 'Laptop', 1200, 10)
        stock.update_item(1, updated_item)
        self.assertEqual(stock.items[1].price, 1200)

    def test_get_item(self):
        stock = Stock()
        item = Item(1, 'Laptop', 1000, 5)
        stock.add_item(item)
        retrieved_item = stock.get_item(1)
        self.assertEqual(retrieved_item.name, 'Laptop')

    def test_list_items(self):
        stock = Stock()
        item1 = Item(1, 'Laptop', 1000, 5)
        item2 = Item(2, 'Mouse', 20, 50)
        stock.add_item(item1)
        stock.add_item(item2)
        items = stock.list_items()
        self.assertEqual(len(items), 2)

if __name__ == '__main__':
    unittest.main()
