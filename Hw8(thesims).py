import random
class Human:
    def __init__(self, name="John Pork", home="None", education=0):
        self.name = name
        self.job = JobGiver
        self.education = education
        self.home = home
        self.money = 0
        self.saturation = 50
        self.gladness = 50
        self.car = Car(brands_of_car, Human)
    def moneyy(self):
        self.money = self.money
    def eat(self):
        House.food -= 1
        if House.food == 0:
            House.food += 10
            self.money -= 10
    def car(self):
        self.car = self.car
    def check_education(self):
        self.education = random.randint(1,3)
    def get_home(self):
        if self.money >= 1000000:
            self.home = House
            self.money -= 1000000

    def get_car(self):
        self.car = Car( brands_of_car, self)

    def to_repair(self):
        self.car.strength += 10
        self.car.fuel += 50
    def get_job(self):
        if self.car.drive():
            jobgiver = JobGiver(Human.check_education)
            jobgiver.give_job()
            self.job = Job(list_of_jobs)
        else:
            self.to_repair()
            return
class House:
    def __init__(self, human):
        self.foodcost = 10
        self.food = 0
        self.trash = 0
        self.humam = human
        self.human = Human
        self.money = human.money
    def foodcost(self):
        self.foodcost = 10
    def food(self):
        self.food = self.food
    def bringfood(self):
        if self.humam.moneyy >= self.foodcost and self.food == 0:
            self.humam.moneyy -= 10
            self.food += 10


class JobGiver:
    def __init__(self, education):
        self.education = education
        self.salary =  Job.salary
        self.gladness_loss = Job.gladness_loss

    def give_job(self):
        if self.education == 1:
            self.salary -= 40
            self.gladness_loss += 15
        elif self.education == 2:
            self.gladness_loss += 5
        elif self.education == 3:
            self.salary += self.salary
            self.gladness_loss -= 5



brands_of_car = {
"BMW": {"fuel": 100, "strength": 100,"consumption": 6, "price": 100000},
"Lada": {"fuel": 50, "strength": 40,"consumption": 10, "price": 5000},
"Volvo": {"fuel": 70, "strength": 150,"consumption": 8, "price": 35000},
"Ferrari": {"fuel": 80, "strength": 120,"consumption": 14, "price": 800000},
}
class Car:
    def __init__(self, brand_list, human):
        self.brand = random.choice(list(brand_list))
        self.human = human
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.price = brand_list[self.brand]["price"]
    def buy(self):
        if self.human.money >= self.price:
            self.human.money -= self.price
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
list_of_jobs = {
"Java developer":{"salary":5000, "gladness_loss": 10 },
"Python developer":{"salary":4000, "gladness_loss": 3 },
"C++ developer":{"salary":4500, "gladness_loss": 25 },
"Rust developer":{"salary":7000, "gladness_loss": 1 },}
class Job:
    def __init__(self, joblist):
        self.job = random.choice(list(joblist))
        self.salary = joblist[self.job]["salary"]
        self.gladness_loss = joblist[self.job]["gladness_loss"]
    def salary(self):
        self.salary = list_of_jobs[self.job]["salary"]
    def gladness_loss(self):
        self.gladness_loss = list_of_jobs[self.job]["gladness_loss"]
human1 = Human()
house1 = House(human1)
job1 = Job(list_of_jobs)
jobgive1 = JobGiver(human1.check_education)
car1 = Car(brands_of_car, human1)