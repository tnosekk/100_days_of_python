import json
from random import choice, randint, shuffle
from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generating random password including letters, numbers, and symbols"""
    letters = [
        "a",
        "b",
        "d",
        "c",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(index=0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save password and mail for given website and store it in data.json file`"""
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) != 0 and len(password) != 0 and len(email) != 0:
        try:
            with open(
                file="day29/password-manager/data.json", mode="r", encoding="utf-8"
            ) as file:
                data = json.load(file)

        except FileNotFoundError:
            with open(
                file="day29/password-manager/data.json", mode="w", encoding="utf-8"
            ) as file:
                file.write("{}")
        else:
            data.update(new_data)
            with open(
                file="day29/password-manager/data.json", mode="w", encoding="utf-8"
            ) as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="Don't leave any field empty")


# ---------------------------- SEARCH  ------------------------------- #


def find_password():
    """Finding password and email based on given website on website entry"""
    website = website_entry.get()
    try:
        with open(
            file="day29/password-manager/data.json", mode="r", encoding="utf-8"
        ) as data:
            website_data = json.load(data)
            email = website_data[website]["email"]
            password = website_data[website]["password"]
    except KeyError:
        messagebox.showinfo(title="error", message="Website not found")
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No Data File Found")
    else:
        messagebox.showinfo(
            title="Website credentials", message=f"email: {email}\npasssord: {password}"
        )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

my_pass_img = PhotoImage(file="day29/password-manager/logo.png")
canvas.create_image(140, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, padx=0)


add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
