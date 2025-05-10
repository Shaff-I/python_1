import random
class Studentname:

    def __init__(self):
        self.randomname2 = random.choice(["Бондарук", "Карась", "Поліщук", "Шафорост", "Мельник", "Шевченко", "Ковальчук", "Бойко", "Траченко", "Ткачук"])
        self.randomname1 = None
        self.name = random.randint(1, 2)
    def namefinder(self):
        self.name = self.name

class Report_card:
    def __init__(self, studentsname):
        self.class1 = "Природознавство"
        self.class2 = "Іноземна мова"
        self.class3 = "Математика"
        self.class4 = "Українська мова/Письмо"
        self.class5 = "Історія України"
        self.class6 = "Всесвітня історія"
        self.class7 = "Основи здоров'я"
        self.class8 = "Образотворче мистецтво"
        self.class9 = "Музичне мистецтво"
        self.class10 = "Зарубіжна література"
        self.class11 = "Українська література"
        self.class12 = "Географія"
        self.class13 = "Інформатика"
        self.class14 = "Дизайн і технології"
        self.class15 = "Фізична культура"
        self.grade1 = random.randint(3,12)
        self.grade2 = random.randint(5,12)
        self.grade3 = random.randint(2,12)
        self.grade4 = random.randint(6,12)
        self.grade5 = random.randint(1,12)
        self.grade6 = random.randint(1,12)
        self.grade7 = random.randint(6,12)
        self.grade8 = random.randint(9,12)
        self.grade9 = random.randint(10,12)
        self.grade10 = random.randint(4,12)
        self.grade11 = random.randint(5,12)
        self.grade12 = random.randint(1,12)
        self.grade13 = random.randint(10,12)
        self.grade14 = random.randint(5,12)
        self.grade15 = random.randint(8,12)
        self.classname = random.choice(["А", "Б", "В", "Г", "Д", "Е", "Є", "Ж"])
        self.student = studentsname

    def randomname(self):
        if self.student.name == 1:
            self.student.randomname1 = random.choice(["Марка", "Андрія", "Максима", "Романа", "Ігоря", "Арсена", "Артема", "Карася", "Влада", "Миколи"])
        elif self.student.name == 2:
            self.student.randomname1 = random.choice(["Олени", "Дар'ї", "Анастасії", "Катерини", "Марії", "Валерії", "Олександри", "Окуня", "Наталії", "Марини"])
        self.student.name = f"{self.student.randomname2} {self.student.randomname1}"

    def reportcard(self):
        self.randomname()
        if self.student.randomname1 == "Ігор" and self.student.randomname2 == "Шафорост":
            self.grade1 = 12
            self.grade2 = 12
            self.grade3 = 12
            self.grade4 = 12
            self.grade5 = 12
            self.grade6 = 12
            self.grade7 = 12
            self.grade8 = 12
            self.grade9 = 12
            self.grade10 = 12
            self.grade11 = 12
            self.grade12 = 12
            self.grade13 = 12
            self.grade14 = 12
            self.grade15 = 12

        print("=" * 12, "Табель за 6 клас", "=" * 12)
        print(f"Учня 6-{self.classname} класу, {self.student.name} ")
        print("Предмет:            ", "Оцінка:")
        print(f"{self.class1}============{self.grade1}")
        print(f"{self.class2}=============={self.grade2}")
        print(f"{self.class3}================={self.grade3}")
        print(f"{self.class4}====={self.grade4}")
        print(f"{self.class5}============{self.grade5}")
        print(f"{self.class6}=========={self.grade6}")
        print(f"{self.class7}============{self.grade7}")
        print(f"{self.class8}====={self.grade8}")
        print(f"{self.class9}=========={self.grade9}")
        print(f"{self.class10}======={self.grade10}")
        print(f"{self.class11}======{self.grade11}")
        print(f"{self.class12}=================={self.grade12}")
        print(f"{self.class13}================{self.grade13}")
        print(f"{self.class14}========{self.grade14}")
        print(f"{self.class15}==========={self.grade15}")
        print("=" * 42)

student1 = Studentname()
report1 = Report_card(student1)
report1.reportcard()