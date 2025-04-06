class Student:
    print("Hello world")
    def __init__(self, height=164):
        self.height = height
        print("My height = ", self.height)\


Artem = Student()
Mark = Student(height = 178)