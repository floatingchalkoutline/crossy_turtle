from turtle import Turtle

STARTING_POSITION = (0, -280)
HEADING = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_start()
        self.setheading(HEADING)

    def crawl(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def reset_start(self):
        self.goto(STARTING_POSITION)

    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

