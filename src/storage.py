class StockItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def get_product(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def reduce_stock(self, product_name, amount):

        stock_item = self.get_product(product_name)

        if not stock_item:
            raise ValueError(f'Product {product_name} not found in stock')
        
        elif stock_item.amount < amount:
            raise ValueError(f"Not enough in stock!")
        
        else:
            stock_item.amount -= amount
            return None
        