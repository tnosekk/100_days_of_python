from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    title_label.config(text="Timer")
    session_count.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
from math import floor


def count_down(count):
    minutes = floor(count / 60)
    seconds = count % 60
    seconds = f"0{seconds}" if seconds < 10 else seconds
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(floor(reps / 2)):
            marks += "✓"
        session_count.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/pomodoro-timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

session_count = Label(text="", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
session_count.grid(column=1, row=3)

start_b = Button(
    text="start",
    width=1,
    borderwidth=0,
    highlightthickness=0,
    highlightbackground=YELLOW,
    command=start_timer,
)
start_b.grid(column=0, row=2)
reset_b = Button(
    text="reset",
    width=1,
    borderwidth=0,
    highlightthickness=0,
    highlightbackground=YELLOW,
    command=reset_timer,
)
reset_b.grid(column=2, row=2)


window.mainloop()
