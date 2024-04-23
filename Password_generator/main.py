from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*']

def generate_password():

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    print("Password is copied to the clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Whoops!!", message="Please do not leave any of the fields empty.")
    else:
        try:
            with open("password.json", "r") as file:
            #reading-"r"(read) the old data and then updating it with the new information
                data = json.load(file)
        except FileNotFoundError:
            #if the json file does not exist then create-"w"(write) a json file, the indent value is used to get the information to be arranged in a way that is eacy for us to read
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #updating the json file
            #what happens here is that the new_data needs to be updated and then it has to be written to the file which is ehy after update, the json.dump() is used again to write the updated dictionary to the file
            #observe that the writing part of the code is repetitive and so this code can be reduced by writing a method but for learning sake this is being done twice
            data.update(new_data)

            with open("password.json", "w") as file:
                #saving the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image) #the tuple here is the coordinate for the image centered in the canvas
canvas.grid(column=1, row=0)

#website
website_label= Label(text="Website:", font=("Arial", 10, "bold"), bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

#Email/Username
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"), bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "afsara.hannan7@gmail.com") #default value insert in the email text box

#password
password_label = Label(text="Password:", font=("Arial", 10, "bold"), bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

#search button
def search_password():
    website = website_entry.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Whoops!!", message="No password file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error!!", message=f"No details for the {website} exist.")


search_button = Button(text="Search", width=7, bg='white', command=search_password)
search_button.grid(column=2, row=1)

#add button

add_button = Button(text="Add", width=32, bg= 'white', command=add_information)
add_button.grid(column=1, row=4, columnspan=2)


#generate button
generate_button = Button(text="Generate", bg='white', width=7, command=generate_password)
generate_button.grid(column=2, row=3)

window.mainloop()