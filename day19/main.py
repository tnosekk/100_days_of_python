from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.pencolor("red")
tim.pensize(2)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    angle = tim.heading() - 10
    tim.setheading(to_angle=angle)


def turn_left():
    angle = tim.heading() + 10
    tim.setheading(to_angle=angle)


def clear_screen_and_move_to_home():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen_and_move_to_home)


screen.exitonclick()
