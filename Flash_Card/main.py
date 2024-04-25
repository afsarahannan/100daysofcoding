from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- UI SETUP ------------------------------- #



window=Tk()
window.title("Flashcard")
window.geometry("900x700")
window.config(padx=100, pady=100, bg="#94dad8")

canvas = Canvas(width=700, height=500, bg='#94dad8', highlightthickness=0)
green_board_image = PhotoImage(file="round_rectangle.png")
canvas.create_image(350,250,image=green_board_image)
canvas.grid(column=1,row=1)


window.mainloop()