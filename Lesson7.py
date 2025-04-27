class Human:
    def __init__(self, name="Name"):
        self.name = name

class Car:
    def __init__(self, brand="Porsche"):
        self.brand = brand
        self.passengers = []
    def add_passengers(self, *args):
        for i in args:
            self.passengers.append(i)
    def print_passengers(self):
        if self.passengers!=[]:
            print(f"Names of {self.brand} passengers:")
            for i in self.passengers:
                print(i.name)
        else:
            print(f"In the car {self.brand} there are no passengers")
dima = Human("Dmytro")
ihor = Human("Ihor")
car1 = Car("Mercedes")
car2 = Car()
car2.add_passengers(ihor, dima)
car2.print_passengers()