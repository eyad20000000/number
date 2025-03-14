print("hhhhhhhhh")

import random
n = random.randint(1,100)
guess = None
while guess != n:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        print("You got it!")
        break
print("Game over!")
x = input("Enter the number: ")
print("You entered:", x)

