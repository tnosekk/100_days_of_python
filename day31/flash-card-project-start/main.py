import time
from random import choice
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flash_cards = {}


# ----- READING DATA ----- #

try:
    words = pd.read_csv("day31/flash-card-project-start/data/to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("day31/flash-card-project-start/data/french_words.csv")
    flash_cards = words.to_dict(orient="records")
else:
    flash_cards = words.to_dict(orient="records")


def next_card():
    """Generates new flash card with a random word from list of french words"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(flash_cards)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="#000000")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="#000000")
    canvas.itemconfig(flashcard, image=flash_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="#FFFFFF")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="#FFFFFF")
    canvas.itemconfig(
        flashcard,
        image=flash_back,
    )


def is_known():
    flash_cards.remove(current_card)
    data = pd.DataFrame(flash_cards)
    data.to_csv("day31/flash-card-project-start/data/to_learn.csv", index=False)

    next_card()


# ----- UI ---- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_back = PhotoImage(file="day31/flash-card-project-start/images/card_back.png")
flash_front = PhotoImage(file="day31/flash-card-project-start/images/card_front.png")
flashcard = canvas.create_image(400, 263)
card_title = canvas.create_text(
    400,
    150,
    font=("Ariel", 40, "italic"),
)
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), fill="#000000")
canvas.grid(column=0, row=0, columnspan=2)


right_image = PhotoImage(file="day31/flash-card-project-start/images/right.png")
button1 = Button(
    image=right_image,
    borderwidth=0,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
    command=is_known,
)
button1.grid(column=1, row=1)

wrong_image = PhotoImage(file="day31/flash-card-project-start/images/wrong.png")
button2 = Button(
    image=wrong_image,
    borderwidth=0,
    highlightthickness=0,
    highlightcolor=BACKGROUND_COLOR,
    command=next_card,
)
button2.grid(column=0, row=1)


next_card()

window.mainloop()
