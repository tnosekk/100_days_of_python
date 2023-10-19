import turtle
from turtle import Turtle, Screen
import random as rand

tim = Turtle()
turtle.colormode(255)


tim.hideturtle()
tim.speed('fastest')
tim.pensize(10)
# colors = ["red", "green", "SkyBlue", "VioletRed3", "RoyalBlue", "SeaGreen3", "MediumOrchid", "IndianRed1"]


def rand_turn():
    directions = [0, 90, 180, 270]
    tim.setheading(rand.choice(directions))


def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


for _ in range(200):
    rgb = random_color()
    tim.color(rgb)
    rand_turn()
    tim.forward(30)

screen = Screen()
screen.exitonclick()
