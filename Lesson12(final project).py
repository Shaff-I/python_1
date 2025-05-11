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
class Headphone_block(Gadget_Aisle):
    def __init__(self, gadget):
        super().__init__(gadget)
        self.thing = gadget
        self.price = 0.0
        if self.gadget == "wireless headphones":
            self.price = 150.0
        elif self.gadget == "headphones with wires":
            self.price = 50.0

class Cash_register(Headphone_block):
    def __init__(self, gadget):
        super().__init__(gadget)
    def buy(self, gadget):
        print(f"Bought item {gadget.gadget} for {gadget.price}$")

rozetka = Store()
gadgetisle1 = Gadget_Aisle("computer")
headphones1 = Headphone_block("wireless headphones")
cashregister1 = Cash_register(gadgetisle1)
cashregister1.buy(gadgetisle1)
cashregister1.buy(headphones1)