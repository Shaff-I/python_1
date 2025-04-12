class Car:
    def __init__(self, make, model, year):
#make це марка машини
        self.make = make
#model це модель машини
        self.model = model
#year це рік випуску машини
        self.year = year
    def get_info(self, year, make, model):
        if year > 1885 and year < 2026:
            print("This guy right here is a", year, make, model)
        else:
            print("You're lying, bro. Ain't no way you got a car from", year, "🤣")

mycar = Car("Chevrolet", "Impala", 1967)
mycar.get_info(1967, "Chevrolet", "Impala")
print("miaw miaw miaw miaw")