number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
action = input("Enter action (+, -, *, /): ")
if action == "+":
    result = number1 + number2
    print(result)
elif action == "-":
    result = number1 - number2
    print(result)
elif action == "*":
    result = number1 * number2
    print(result)
elif action == "/":
    result = number1 / number2
    print(result)
elif (number1 == 0 and action == "/") or (number2 == 0 and action == "/"):
    result = number1 - number2
    print(result)