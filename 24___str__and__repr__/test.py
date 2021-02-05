# 1. The __init__ method, which should take an argument, name. It should initialize self.name to be the argument,
#     and self.items to be an empty list

2. The add_item method, which should append a dictionary representing an item to the store's itme property.
The dictionary should have keys name and price.

3. The stock_price method, which should add up each item price inside self.items to come up with a total, and return that.

class Store:
    def __init__(self, name, []):
        self.name = name
        self.itmes = []

        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)
        
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        
        # total = 0
        # for item in self.items:
        #     total += item['price'] 
        # return total
        return sum(item['price'] for item in self.items )


