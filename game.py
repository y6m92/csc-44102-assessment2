import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1,20)
attempts = 0 
max_attempts = 5
guess_input = 0

print("I am thinking of a number between 1 to 20.")
print("You have 5 attempts to guess the number.")

while guess_input != number and attempts < max_attempts: 
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess_input = int(guess)
    attempts += 1
    
    #Game Logic
    if guess_input < number:
        print("Too low! Try again..")
    elif guess_input > number:
        print("Too high! Try again..")
    else:
        print("Congratulations! You guessed it right.")
        print("Number of attempts: ", attempts)
        break
    
    if attempts == max_attempts:
        print("You have used all your attempts. Game over!")
        print("The correct number was:",number)


