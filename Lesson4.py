color = input("Enter 1 of 3 colors: red, green, yellow:  ")
while color != "green":
    if color == "red":
        print("Red light -- stop")
        color = input("Enter 1 of 3 colors: red, green, yellow:  ")
    elif color == "yellow":
        print("Yellow light -- wait")
        color = input("Enter 1 of 3 colors: red, green, yellow:  ")
    else:
        print("error")
        color = input("Enter 1 of 3 colors: red, green, yellow:  ")
if color == "green":
    print("Green light -- go")
    color = input("Enter 1 of 3 colors: red, green, yellow:  ")
