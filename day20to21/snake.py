from turtle import Turtle

STARTING_POSTITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()

    def create_snakes(self):
        for pos in STARTING_POSTITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setpos(STARTING_POSTITIONS[pos])
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
        self.segments[0].forward(20)
