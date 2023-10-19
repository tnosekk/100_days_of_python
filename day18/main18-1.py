from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
