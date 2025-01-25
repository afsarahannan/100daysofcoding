import requests
from tkinter import *
def quote_gen():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    print(data)
    canvas.itemconfig(quote_text, text=data['quote'], font=('Arial', 20, 'bold'))

window = Tk()
window.title("Kanye says...")
# window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=500)
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 280, image = background_img)
quote_text=canvas.create_text(200,190,text="    Kanye\n      The\nAll-Knowing", width=300, font=('Arial', 30, 'bold'), fill='black')
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Kanye_emoji.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=quote_gen)
kanye_button.grid(row=1, column=0)


window.mainloop()
