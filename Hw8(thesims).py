import random
class Human:
    def __init__(self, name="John Pork", home="None", education = 0):
        self.name = name
        self.job = JobGiver
        self.education = education
        self.home = home
        self.money = 10000.0
        self.saturation = 50
        self.gladness = 50
        self.car = Car(brands_of_car)
    def money(self):
        self.money = self.money
    def eat(self):
        House.food -= 1
        if House.food <= 0:
            House.food += 10
            self.money -= 10
    def buyfood(self):
        self.money -= 10
    def car(self):
        self.car = self.car
    def education(self):
        self.education = random.randint(1,3)
    def get_home(self):
        if self.money >= 1000000:
            self.home = House()
            self.money -= 1000000

    def get_car(self):
        self.car = Car(brands_of_car)

    def to_repair(self):
        self.car.strength += 10
        self.car.fuel += 50
    def get_job(self):
        if self.car.drive:
            self.job.give_job(self)
        else:
            self.to_repair()
            return
        self.job = Job(joblist)
class House:
    def __init__(self):
        self.food = 0
        self.trash = 0
        self.human = Human
    def food(self):
        self.food = self.food
    def bringfood(self):
        if Human.money >= 10 and self.food == 0:
            Human.buyfood()
            self.food += 10


class JobGiver:
    def __init__(self):
        self.education = Human.education
        self.salary =  Job.salary
        self.gladness_loss = Job.gladness_loss

    def give_job(self):
        if self.education == 1:
            self.salary -= 40
            self.gladness_loss += 15
        elif self.education == 2:
            self.gladness_loss += 5
        if self.education == 3:
            self.salary += self.salary
            self.gladness_loss -= 5



brands_of_car = {
"BMW": {"fuel": 100, "strength": 100,"consumption": 6, "price": 100000},
"Lada": {"fuel": 50, "strength": 40,"consumption": 10, "price": 5000},
"Volvo": {"fuel": 70, "strength": 150,"consumption": 8, "price": 35000},
"Ferrari": {"fuel": 80, "strength": 120,"consumption": 14, "price": 800000},
}
class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.price = brand_list[self.brand]["price"]
    def buy(self):
        if Human.money() >= self.price:
            pass
        else:
            print("Can't afford car")
            Human.car = "None"
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car can't move")
            return False
joblist = {
"Java developer":{"salary":50, "gladness_loss": 10 },
"Python developer":{"salary":40, "gladness_loss": 3 },
"C++ developer":{"salary":45, "gladness_loss": 25 },
"Rust developer":{"salary":70, "gladness_loss": 1 },}
class Job:
    def __init__(self, joblist):
        self.job = random.choice(list(joblist))
        self.salary = joblist[self.job]["salary"]
        self.gladness_loss = joblist[self.job]["gladness_loss"]
    def salary(self):
        self.salary = joblist[self.job]["salary"]
    def gladness_loss(self):
        self.gladness_loss = joblist[self.job]["gladness_loss"]