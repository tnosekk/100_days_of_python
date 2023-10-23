from random import randint
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=350)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

# turtle1 = Turtle(shape="turtle")
# turtle1.penup()
# turtle1.color("purple")
# turtle1.goto(x=-330, y=-100)

y_cord = -120
for t_color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(t_color)
    turtle.goto(x=-230, y=y_cord)
    y_cord += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
