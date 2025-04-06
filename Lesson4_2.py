def calculator(x1, x2, op):
    if op == "+":
        print("Result: ",x1 + x2)
    elif op == "-":
        print("Result: ",x1 - x2)
    elif op == "/":
        if x2 == 0:
            print("You can't divide by zero")
        else:
            print("Result: ",x1 / x2)
    elif op == "*":
        print("Result: ",x1 * x2)



a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
operation = input("Enter the action(+, -, /, *): ")

calculator(a, b, operation)