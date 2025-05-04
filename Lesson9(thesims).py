import random
class Human:
    def __init__(self, name="John Pork", job="None", home="None", car="None" ):
        self.name = name
        self.job = Job
        self.home = home
        self.car = car
        self.money = 100.0
        self.saturation = 50
        self.gladness = 50
    def get_home(self):
        self.home = House()

    def to_repair(self):
        self.money -= 25
        self.car.strength = 100
    def get_car(self):
        self.car = Car(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_loss
        self.job = Job(job_list)

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption():
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.car.fuel += 100
            self.money -= 100
            print("I bought fuel")
        if manage == "food":
            self.home.food += 50
            self.money -= 50
            print("I bought food")
        if manage == "delicacies":
            self.gladness += 10
            self.home.food += 2
            self.money -= 10
            print("I bought delicacies!!!")
    def days_indexes(self, day):
        day = f" Today's the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.saturation}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.trash}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
    def is_alive(self):
        if self.saturation <= 0:
            print("Dead...")
            return False
        if self.money <= -500:
            print("Broke...")
            return False
        if self.gladness <= 0:
            print("Depressed...")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print("Settled in the house!")
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f"I bought a {self.car.brand}!")
        if self.job == None:
            self.get_job()
            print(f"Gonna get a job {self.job.job}, with salary {self.job.salary}")
        self.days_indexes(day)
        if self.saturation <= 20:
            print("I'm gonna go eat something")
            self.eat()
        elif self.gladness < 20:
            if self.home.trash >= 20:
                print("I gotta clean my house")
                self.clean()
            else:
                print("Aight bet!")
                self.chill()
        elif self.money < -50:
            print("I gotta work")
            self.work()
        dice = random.randint(1, 4)
        if dice == 1:
            print("Aight bet!")
            self.chill()
        elif dice == 2:
            print("I gotta work")
            self.work()
        elif dice == 3:
            print("I gotta clean my house")
            self.clean()
        elif dice == 4:
            print("Alright, time to buy some snacks!")
            self.shopping(manage="delicacies")


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.saturation >= 100:
                return
            else:
                self.saturation += 5
                self.home.food -= 5

    def chill(self):
        self.gladness += 25
        self.home.trash += 5

    def clean(self):
        self.gladness -= 5
        self.home.trash = 0

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <= self.car.consumption:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_loss
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

