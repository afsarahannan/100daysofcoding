from tkinter import *

window = Tk()

window.title("GUI Program")

window.minsize(width=500, height=300)
window.config(padx = 20, pady=20)

#Label
my_label = Label(text="This is a label.", font=("Arial", 10, "bold"))
# my_label.pack() #the packer will centers the label in the center of the screen
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#the text can also be changed like this
my_label["text"] = "text"
my_label.config(text="New Text")


#Button
def button_clicked():
    my_label.config(text=input.get())
    print("Button works just fine.")

button = Button(text="Click to change the title", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#newbutton
# button2 = Button(text="Click to change the title", command=button_clicked)
# # button.pack()
# button2.grid(column=2, row=0)

#Entry
input = Entry(width=30)
input.insert(END, string="Write Something Here.")
# input.pack()
input.grid(column=3, row=2)


#text
text = Text(height=3, width=50)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack(expand=1)

#spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=20, width=3, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Check Button
def checkbutton_used():
    print(checked_state.get())

checked_state= IntVar()
checkbutton = Checkbutton(text= "Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio1 = Radiobutton(text= "Option1", value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text= "Option2", value=2, variable=radio_state, command=radio_used)
radio1.pack()
radio2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', "Pear", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListBoxSelect>>", listbox_used)
listbox.pack()
#


window.mainloop()

