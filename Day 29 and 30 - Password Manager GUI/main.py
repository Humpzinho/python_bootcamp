# ----------------------------- IMPORTS ------------------------------ #

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string
import json

# ---------------------------- CONSTANTS AND VARIABLES ------------------------------- #
FONT = ("SF Compact Display", 12)

# ---------------------------- FIND DATA ------------------------------- #

def find_data():
    
    try:
        with open(file="Day 29 - Password Manager GUI\\data.json",
                          mode="r") as file:
            data = json.load(file)
            email = data[website_entry.get().lower()]["email"]
            password = data[website_entry.get().lower()]["password"]
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            password_entry.insert(0, password)
            email_entry.insert(0, email)
    except:
        messagebox.showinfo(title="Oops...",
                            message="There's no data with this name.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [random.choice(letters) for _ in range(10)]
    nr_symbols = [random.choice(symbols) for _ in range(4)]
    nr_numbers = [random.choice(numbers) for _ in range(4)]

    allchar = nr_letters + nr_numbers + nr_symbols

    random.shuffle(allchar)
    print(allchar)

    password = ''.join(allchar)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get().lower()
    new_data = {website: {"email": email, "password": password}}

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops...",
                            message="Don't leave any fields blank.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=
            f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIt is ok to save?"
        )

        if is_ok:
            try:
                with open(file="Day 29 - Password Manager GUI\\data.json",
                          mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
                    
            except:
                with open(file="Day 29 - Password Manager GUI\\data.json",
                          mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open(file="Day 29 - Password Manager GUI\\data.json",
                          mode="w") as file:
                    json.dump(data, file, indent=4)
                    
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                is_ok = False


# ---------------------------- UI SETUP ------------------------------- #

#WINDOW SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
from tkinter.ttk import *

#CANVAS SETTINGS
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Day 29 - Password Manager GUI\logo.png")
canvas.create_image(100, 100, image=logo)

#LABELS
website_label = Label(text="Website:", font=FONT)
email_label = Label(text="Email/Username:", font=FONT)
password_label = Label(text="Password:", font=FONT)

#BUTTONS
gen_pass_button = Button(text="Generate Password", command=gen_pass)
add_button = Button(text="Add", command=save)
search_button = Button(text="Search", command=find_data)

#ENTRY
website_entry = Entry(width=40)
website_entry.focus()
email_entry = Entry()
email_entry.insert(0, "srdrone@hotmail.com")
password_entry = Entry()

#GRID
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, sticky="EW")
email_entry.grid(column=1, row=2, sticky="EW", columnspan=2)
password_entry.grid(column=1, row=3, sticky="EW")

gen_pass_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
