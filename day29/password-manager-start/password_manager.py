from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

my_pass_img = PhotoImage(file="day29/password-manager-start/logo.png")
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
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, padx=0)
add_button = Button(width=36, text="Add")
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
