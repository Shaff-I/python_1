import random
class Human:
    def __init__(self):
        self.id = random.randint(100000000000, 999999999999)
        self.age = random.randint(1, 99)
        self.birthday = random.randint(1, 31)
        self.birthmonth = random.randint(1, 4)
        self.birthyear = 2025 - self.age
        self.birth = f"{self.birthday:02}.{self.birthmonth:02}.{self.birthyear}"
        self.gender_code = random.randint(1, 2)
        self.gender = "Male" if self.gender_code == 1 else "Female"
        self.name1_id = random.randint(1, 8)
        self.name2_id = random.randint(1, 8)
        self.name1 = self.generate_name1()
        self.name2 = self.generate_name2()
        self.job_id = random.randint(1, 10)
        self.job = self.generate_job()
        self.education_id = random.randint(0, 3)
        self.education = self.generate_education()
        self.drinkage = "True" if self.age >= 18 else "False"
        if self.birthmonth == 2:
            self.birthday = random.randint(1, 28)

    def generate_name1(self):
        male_names = ["John", "Barry", "Zoro", "Hawk", "Michael", "Muzan", "Ben", "Dmytro"]
        female_names = ["Mia", "Juan", "Elisabeth", "Alison", "Miss", "Jenny", "Hawk", "Katherine"]
        return male_names[self.name1_id - 1] if self.gender == "Male" else female_names[self.name1_id - 1]

    def generate_name2(self):
        lastnames = ["Pork", "Obama", "Chungus", "Tuah", "Jackson", "Jordan", "Dover", "HooLee-Sheet"]
        return lastnames[self.name2_id - 1]

    def generate_job(self):
        jobs = ["Electrician", "Barbarian", "Teacher", "None", "Basketball player",
                "Singer", "Principal", "IT-programmer", "Janitor", "Singer"]
        if self.age >= 18:
            return jobs[self.job_id - 1]
        else:
            self.job = "None"
            self.education = "None"

    def generate_education(self):
        levels = ["None", "Low", "Middle", "High"]
        return levels[self.education_id]


class Passport:
    def __init__(self, human):
        self.idnumber = human.id
        self.birthday = human.birth
        self.gender = human.gender
        self.name1 = human.name1
        self.name2 = human.name2
        self.age = human.age
        self.job = human.job
        self.education = human.education
        self.drinkingage = human.drinkage
        self.dateofhanding = "02.05.2025"

    def show(self):
        print("=================== Passport ===================")
        print(f"Gender: {self.gender}")
        print(f"Full legal name: {self.name1} {self.name2}")
        print(f"Birthday: {self.birthday}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Education: {self.education}")
        print(f"Past legal drinking age? {self.drinkingage}")
        print(f"Date of passport giveaway: {self.dateofhanding}")
        print(f"Passport ID: {self.idnumber}")
        print("===============================================")
human1 = Human()
passport1 = Passport(human1)
passport1.show()
