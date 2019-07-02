class Store:
    def __init__(self, name, product):
        self.item_name = name
        self.products = product

class Product:
    def __init__(self, name, cost, categories):
        self.item_name = name
        self.price = cost
        self.category = categories
        self.status = "for sale"

    def display_info(self):
        print("Item Name: " + str(self.item_name))
        print("Price: " + str(self.price))
        print("Category: " + str(self.category))
        print("Status: " + str(self.status))
        return self

    def sell(self):
        self.status = "sold"
        return self