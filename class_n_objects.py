# This is a small python snippet which introduces how to create a class with a constructor,
# some functions inside the class and their usage.

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        ''' A function to add items in store list '''
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        ''' A function to calculate cost of stocks '''
        total = 0
        for item in self.items:
            total += item["price"]
        return (total)

# Creating an instance of object
x = Store("Security Books")

# Adding items in stock
x.add_item("Gray Hat Hacking", 34)
x.add_item("Rafay Baloch", 34.42)

# Total of stock items
print("The total of items is: ", x.stock_price())
