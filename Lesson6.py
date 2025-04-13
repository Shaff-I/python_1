class Student:
    number = 0
    def __init__(self, height=164, name = None):
        self.height = height
        self.name = name
        Student.number = Student.number + 1
    def grow(self, height = 3):
        self.height = self.height + 1

    def __str__(self):
        return f"I'm a student named {self.name}, my height is {self.height}"

Artem = Student(name = "Artem")
Mark = Student(height = 178, name = "Mark")

print(Artem)
print(Mark)

while Mark.height < 180:
    Mark.grow()
print(Artem)
print(Mark)

print("Number of students = ", Student.number)

