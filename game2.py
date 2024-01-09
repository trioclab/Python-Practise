  # Guess game in Python
# importing module 
import random

x = 10
def guess(x):
    # randint will generate the random integer from the module
    random_number = random.randint(1,x)
    # As we have defined number start from 1 so for further while condition I assme that guess = 0
    guess = 0
    while guess != random_number :
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess > random_number:
            print("Wrong Guess , A little high ")
        elif guess < random_number:
            print("Wrong Guess , A little low ")
    print(f"Congrats !!! You have guess the correct number: {random_number}.")
# Calling function guess
guess(x)