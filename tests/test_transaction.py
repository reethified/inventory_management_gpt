import unittest
from models import Transaction, Item

class TestTransaction(unittest.TestCase):
    def test_calculate_total_amount(self):
        item1 = Item(1, 'Laptop', 1000, 2)
        item2 = Item(2, 'Mouse', 20, 5)
        transaction = Transaction(1, [item1, item2], 0)
        transaction.calculate_total_amount()
        self.assertEqual(transaction.total_amount, 2020)

if __name__ == '__main__':
    unittest.main()
