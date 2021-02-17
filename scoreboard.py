from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-210, 260)
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER! YOUR SCORE: {self.level - 1}", move=False, align="center", font=FONT)
