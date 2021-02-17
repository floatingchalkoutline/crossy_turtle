from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_CAR_YCOR = range(-240, 260)
STARTING_CAR_XCOR = 340
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.traffic = []
        self.level_speed = 1

    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setx(STARTING_CAR_XCOR)
        car.sety(random.choice(STARTING_CAR_YCOR))
        self.traffic.append(car)

    def drive(self):
        for vehicle in self.traffic:
            vehicle.setx(vehicle.xcor() - (MOVE_INCREMENT * self.level_speed))

    def accelerate(self):
        self.level_speed += 0.5
