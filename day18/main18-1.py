from turtle import Screen, Turtle

tim = Turtle()
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
