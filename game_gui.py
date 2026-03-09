import tkinter as tk
import random

#Create game window
app = tk.Tk()
app.title("Number Guessing Game")

#Game values
number = random.randint(1,20)
tries = 0
max_tries = 5

def check_guess():
    global tries
    guess = entry.get()
    
    if not guess.isdigit():
        feedback_label.config(text="Enter a number.")
        return
    
    guess = int(guess)
    tries += 1
    tries_label.config(text=f"Attempts: {tries}/{max_tries}")
    
    if guess < number:
        feedback_label.config(text="Too low.")
    elif guess > number:
        feedback_label.config(text="Too high.")
    else:
        feedback_label.config(text="Correct!")
        submit.config(state="disabled")
        return
    
    if tries == max_tries:
        feedback_label.config(text=f"Out of tries. Number was {number}.")
        submit.config(state="disabled")
        
#title
title = tk.Label(app, text="Guess the number between 1 and 20")
title.pack()

#attempts   
tries_label = tk.Label(app, text=f"Attempts: {tries}/{max_tries}")
tries_label.pack()

#input box
entry = tk.Entry(app)
entry.pack()

#feedback text 
feedback_label = tk.Label(app, text="")
feedback_label.pack()

#button 
submit = tk.Button(app, text="Submit guess", command=check_guess)
submit.pack()

app.mainloop()