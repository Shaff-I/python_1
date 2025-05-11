class Store:
    def __init__(self):
        self.price = 0.0

class Gadget_Aisle(Store):
    def __init__(self, gadget):
        super().__init__()
        self.gadget = gadget
        self.price = 0.0
        if self.gadget == "computer":
            self.price = 900.0
        elif self.gadget == "phone":
            self.price = 150.0
        elif self.gadget == "tablet":
            self.price = 200.0
        elif self.gadget == "console":
            self.price = 300.0
        elif self.gadget == "laptop":
            self.price = 550.0
        elif self.gadget == "TV":
            self.price = 1000.0
    def buy(self):
        print(f"Bought item {self.gadget} for {self.price}$")
class Headphone_block(Gadget_Aisle):
    def __init__(self, gadget):
        super().__init__(gadget)
        self.gadget = gadget
        self.price = 0.0
        if self.gadget == "wireless headphones":
            self.price = 150.0
        elif self.gadget == "headphones with wires":
            self.price = 50.0
    def buy(self):
        print(f"Bought item {self.gadget} for {self.price}$")
rozetka = Store()
gadgetisle1 = Gadget_Aisle("computer")
headphones1 = Headphone_block("wireless headphones")
gadgetisle1.buy()
headphones1.buy()

'''
class Cash_register(Store, Gadget_Aisle, Headphone_block):
    def __init__(self):
        super().__init__()
        self.price =
'''
