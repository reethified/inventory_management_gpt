class Admin:
    def __init__(self, stock):
        self.stock = stock

    def add_stock_item(self, item):
        self.stock.add_item(item)

    def remove_stock_item(self, item):
        self.stock.remove_item(item)

    def update_stock_item(self, item_name, new_item):
        self.stock.update_item(item_name, new_item)

    def check_stock(self, item_name):
        return self.stock.get_item(item_name)


class Stock:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_item(self, item_name, new_item):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.items[i] = new_item
                break

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def __str__(self):
        return f"Stock item={len(self.items)})"

class Transaction:
    def __init__(self):
        self.sales = []

    def add_sale(self, item, quantity):
        self.sales.append((item, quantity))

    def get_sales_report(self):
        return self.sales

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"