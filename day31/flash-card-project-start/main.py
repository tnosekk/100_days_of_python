from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# ----- UI ---- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_front = PhotoImage(file="day31/flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image=flash_front)
canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"), fill="#000000"
)
canvas.create_text(
    400, 263, text="French word", font=("Ariel", 60, "bold"), fill="#000000"
)


canvas.grid(column=0, row=0, columnspan=2)


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
