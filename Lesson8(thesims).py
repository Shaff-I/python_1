import random
class Human:
    def __init__(self, name="John Pork", job="None", home="None", car="None" ):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100.0
        self.saturation = 50
        self.gladness = 50
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Car(brands_of_car)

    def get_job(self):
        if self.car.drive:
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
class House:
    def __init__(self):
        self.food = 0
        self.trash = 0


brands_of_car = {
"BMW": {"fuel": 100, "strength": 100,"consumption": 6},
"Lada": {"fuel": 50, "strength": 40,"consumption": 10},
"Volvo": {"fuel": 70, "strength": 150,"consumption": 8},
"Ferrari": {"fuel": 80, "strength": 120,"consumption": 14},
}
class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car can't move")
            return False
job_list = {
"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },}
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_loss = job_list[self.job]["gladness_loss"]