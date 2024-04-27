print("~~~~~WElcome to the number guessing game~~~~~")

import random

number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("Enter Guess: "))

    if guess<number:
        print("Computer guess",number)
        print("Computer Guess Higher :")
    elif guess > number:
        print("Computer guess",number)
        print("computer Guess lower :")
    else:
        print("You Won!")
