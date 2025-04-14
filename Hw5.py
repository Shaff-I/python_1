class Employee:
    def __init__(self, name, position, salary=0.0):
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
            return f"{self.name}'s salary is {self.salary}"

job1 = Employee("Joe", "Mama", 1346)
print(job1)