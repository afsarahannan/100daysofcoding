import random
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from random import choice, randint, shuffle

from tkinter import messagebox
import json

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/HSK_1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Chinese', fill="black")
    canvas.itemconfig(card_word, text=current_card['Chinese'], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='Meaning', fill="white")
    canvas.itemconfig(card_word, text=current_card['Meaning'], fill = "white")
    canvas.itemconfig(card, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    next_word()

window=Tk()
window.title("Flashcard")
window.config(padx = 50, pady= 50, bg=BACKGROUND)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526) #this canvas has to be the same size as the image placed on top of it
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 48, "italic"))
canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)

next_word()
print(to_learn)
window.mainloop()