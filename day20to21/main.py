import time
from turtle import Screen

from food import Food
from scoreboard import Score_board
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Score_board()
delay = 0.1


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        delay -= 0.005
        scoreboard.increase_score()

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.reset()
        delay = 0.1

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            delay = 0.1

screen.exitonclick()
