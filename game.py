import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1,20)
attempts = 0 
guess = 0

print("I am thinking of a number between 1 to 20.")

while guess != number:
    guess = int(input("Enter your guess:"))
    attempts += 1
    
    if guess < number:
        print("Too low! Try again..")
    elif guess > number:
        print("Too high! Try again..")
    else:
        print("Congratulations! You guessed it right.")
        print("Number of attempts: ", attempts)


