from tkinter import *

window = Tk()
window.title("Mile to Km convertor")
window.minsize(width=300, height=10)

#Entry
input = Entry(width=5)
input.insert(END, "0")
input.place(x=110, y=30)

#label
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.place(x=160, y=30)

equals_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equals_label.place(x=10, y=70)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.place(x=160, y=70)

answer_label = Label(text="Answer", font=("Arial", 10, "bold"))
answer_label.place(x=90, y=70)


#button
def miles_to_km():
    answer = round(float(input.get())*1.6, 2)
    answer_label.config(text=f"{answer}")
    print("Button works just fine.")

button = Button(text="Calculate", command=miles_to_km)
button.place(x=90, y=90)

window.mainloop()