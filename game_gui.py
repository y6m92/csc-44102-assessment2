import tkinter as tk
import random

#Create game window
app = tk.Tk()
app.title("Number Guessing Game")

#Game values
number = random.randint(1,20)
tries = 0
max_tries = 5

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
submit = tk.Button(app, text="Submit guess")
submit.pack()

app.mainloop()