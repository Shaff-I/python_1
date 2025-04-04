n = int(input("Write number n for the factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The number's factorial is {n} = {factorial}")