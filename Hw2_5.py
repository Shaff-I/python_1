n = int(input("Enter number n:  "))
evennumbers = [str(i) for i in range(n, 0, -1) if i % 2 == 0]
print(" ".join(evennumbers))