from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

button = Button(text="Click")
button2 = Button(text="Click")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)

entry = Entry(width=10)
entry.insert(END, string="Some text")
entry.grid(column=3, row=2)


""" Tkinter widgets
# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of text")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
"""


window.mainloop()
