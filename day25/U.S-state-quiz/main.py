import turtle

import pandas as pd

data = pd.read_csv("day25/U.S-state-quiz/50_states.csv")
states_list = data["state"].to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "day25/U.S-state-quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def check_if_valid_state(state):
    if state in states_list:
        return True
    else:
        return False


guessed_states = 0

while guessed_states <= 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    answer_state = screen.textinput(
        title=f"{guessed_states}/50 Guess the state",
        prompt="What's another state's name?",
    ).title()

    state_data = data[data["state"] == answer_state]
    if check_if_valid_state(answer_state):
        guessed_states += 1
        t.goto(int(state_data.x), int(state_data.y))
        t.write(arg=answer_state)
