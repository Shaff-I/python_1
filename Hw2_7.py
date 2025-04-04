grade = int(input("Enter your grade: "))
if grade > 0 and grade <= 49:
    print("D")
elif grade > 49 and grade <= 69:
    print("C")
elif grade > 69 and grade <= 89:
    print("B")
elif grade > 89 and grade <= 100:
    print("A")
elif grade > 100:
    print("Cheater!!!")