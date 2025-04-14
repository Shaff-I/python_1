import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50.0
        self.progress = 0.0
        self.money = 100.0
        self.day = 1
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.end_of_day()
        self.is_alive()
    def to_work(self):
        print("Gotta work")
        self.gladness -= 7.5
        self.progress += 0.4
        self.money += 50
        self.end_of_day()
        self.is_alive()
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.end_of_day()
        self.is_alive()
    def to_chill(self):
        print("Rest time")
        self.gladness += 15
        self.progress -= 0.1
        self.money -= 35
        self.end_of_day()
        self.is_alive()
    def gift(self):
        cube = random.randint(10, 100)
        chance_cube = random.randint(1, 100)
        if chance_cube == 69:
            print("="*17, "Your mom supported you!", "="*17)
            self.gladness += cube
            self.money += cube
            self.progress += 0.35
    def is_alive(self):
        if self.progress < 0.05:
            print("I have to study or I'll be cast out...")
            self.to_study()
        elif self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 10:
            print("I'm tired...")
            self.to_chill()
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 50:
            print("Passed externally...")
            self.alive = False
        elif self.money <= 10:
            print("I have to work or I'll be broke...")
            self.to_work()
        elif self.money <= 0:
            print("Broke ass...")
            self.alive = False
        elif self.day == 366:
            print("="*17,"Good ending: You survived for a whole year!", "="*17)
            self.money = 1e+100
            self.gladness = 100
            self.progress = 100
            self.end_of_day()
            self.alive = False
    def end_of_day(self):
        self.gift()
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}%")
        print(f"Money = {self.money}")
        self.day += 1
    def live(self):
        daycycle = "Day" + str(self.day) + "of" + self.name + "life"
        print(f"{daycycle:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

nick = Student(name="Nick")
for day in range(365):
    if not nick.alive:
        break
while nick.alive:
    nick.live()

