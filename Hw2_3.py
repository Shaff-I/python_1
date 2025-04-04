import random

secret_number = random.randint(1, 10)
attempts = 3
print("Guess the number from 1 to 10, you have 3 tries.")
for attempt in range(1, attempts + 1):
    guess = int(input(f"Try {attempt}: "))
    if guess > secret_number:
        print("The number is less than ", guess, "!")
    elif guess < secret_number:
        print("The number is more than ", guess, "!")
    else:
        print("Congrats! you guessed the word!")
        break

if guess != secret_number:
    print(f"You lost. The number was", secret_number, ".")
