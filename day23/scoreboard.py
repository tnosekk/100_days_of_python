from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 270)
        self.level = 1
        self.color("Black")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
