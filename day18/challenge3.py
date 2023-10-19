from turtle import Turtle, Screen
import random as r

tim = Turtle()
tim.pensize(2)
colors = ["red", "green", "SkyBlue", "VioletRed3", "RoyalBlue", "SeaGreen3", "MediumOrchid", "IndianRed1"]


def draw_shape(num_sizes):
    angle = 360/num_sizes
    for side in range(num_sizes):
        tim.forward(100)
        tim.right(angle)


for shape_side_num in range(3, 11):
    tim.pencolor(r.choice(colors))
    draw_shape(shape_side_num)


screen = Screen()
screen.exitonclick()
