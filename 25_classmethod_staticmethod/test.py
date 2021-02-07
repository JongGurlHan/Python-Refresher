class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        print(store.name+" - franchise")
        
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f"NAME:{store.name},  " 
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store) #returns a Store with name "Test - franchise"
Store.franchise(store2) #returns a Store with name "Amazon - franchise"
