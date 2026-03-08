import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1,20)
attempts = 0 
guess = 0

print("I am thinking of a number between 1 to 20.")

while guess_input != number:
    guess = input("Enter your guess:")
    
    if not guess.isdigit():
        print("Please enter a number.")
        continue
    
    guess_input = int(guess)
    attempts += 1
    
    if guess_input < number:
        print("Too low! Try again..")
    elif guess_input > number:
        print("Too high! Try again..")
    else:
        print("Congratulations! You guessed it right.")
        print("Number of attempts: ", attempts)


