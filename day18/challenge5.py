import random as rand
import turtle
from turtle import Screen, Turtle

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.pensize(2)


def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def draw_circle_with_color(radius):
    rgb = random_color()
    tim.color(rgb)
    tim.circle(radius)


angle = 0
angle_change = 3
iterations = int(360 / angle_change)

for _ in range(iterations):
    tim.setheading(angle)
    angle += angle_change
    draw_circle_with_color(100)


screen = Screen()
screen.exitonclick()
