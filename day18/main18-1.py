from turtle import Screen, Turtle

tim = Turtle()
for _ in range(25):
    tim.forward(2)
    tim.penup()
    tim.forward(2)
    tim.pendown()

screen = Screen()
screen.exitonclick()
