from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    user_data = f"{website}\t|\t{email}\t|\t{password}\n"

    if len(website) != 0 and len(password) != 0 and len(email) != 0:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are your data:\n"
            f"website: {website}\n"
            f"email: {email}\n"
            f"password: {password}\n"
            "Is this ok to save?",
        )
        if is_ok:
            with open(file="day29/password-manager/data.txt", mode="a") as file:
                file.write(user_data)
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
        else:
            pass
    else:
        messagebox.showwarning(title="Warning", message="Don't leave any field empty")


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

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "email@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, padx=0)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
