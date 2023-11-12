from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# ----- UI ---- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_front = PhotoImage(file="day31/flash-card-project-start/images/card_front.png")
canvas.create_image(450, 300, image=flash_front)
canvas.grid(column=0, row=0, columnspan=2)

french_label = Label(text="French", font=("Arienl", 40, "italic"))
french_label.grid(column=0, row=0, columnspan=2)

french_word = Label(text="french_word", font=("Ariel", 40, "italic"))
french_word.grid(column=0, row=0, columnspan=2)


right_image = PhotoImage(file="day31/flash-card-project-start/images/right.png")
button1 = Button(
    image=right_image,
    borderwidth=0,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
)
button1.grid(column=1, row=1)

wrong_image = PhotoImage(file="day31/flash-card-project-start/images/wrong.png")
button2 = Button(
    image=wrong_image,
    borderwidth=0,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
)
button2.grid(column=0, row=1)

window.mainloop()
