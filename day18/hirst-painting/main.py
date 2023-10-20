import turtle
from turtle import Turtle, Screen
import random as rand
# import colorgram
# def extract_rgb_colours(filename, num_of_colours):
#     """Extract given amount of colours from given image in rgb format in list of tuples"""
#     colors = colorgram.extract(filename, num_of_colours)
#     colors_rgb = []
#     for i in range(num_of_colours):
#         color = colors[i].rgb
#         r = color.r
#         g = color.g
#         b = color.b
#         rgb = (r, g, b)
#         colors_rgb.append(rgb)
#     return colors_rgb
# colours = extract_rgb_colours('image.jpg', 10)

turtle.colormode(255)
tim = Turtle()
tim.ht()
tim.pensize(3)
tim.speed(0)
tim.penup()


colours = [
    (206, 178, 22),
    (19, 117, 160),
    (185, 85, 21),
    (215, 156, 106),
    (66, 24, 4),
    (162, 12, 25),
    (4, 102, 72),
    (15, 29, 52),
    (149, 23, 12)
]

tim.setheading(230)
tim.forward(370)
tim.setheading(0)

for move_y in range(11):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    for move_x in range(11):
        rand_color = rand.choice(colours)
        tim.dot(20, rand_color)
        tim.forward(50)
    tim.back(550)

screen = Screen()
screen.exitonclick()
