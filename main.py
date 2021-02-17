import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# this list is used to randomly decide whether to add a new car or not
TRUE_OR_FALSE = [True, False]

# initialize the screen and setup
screen = Screen()
screen.title("Crossy Turtle!")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# creates the player turtle
player = Player()
# creates the car_manager as a list that maintains all of the cars being randomly generated.
car_manager = CarManager()
# creates the scoreboard
scoreboard = Scoreboard()
# player can only move up
screen.onkey(player.crawl, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    create_car = random.choice(TRUE_OR_FALSE)
    if create_car:
        car_manager.new_car()
    car_manager.drive()
    if player.check_finish_line():
        # if the player reaches the finish line, the player's position resets to the beginning, and cars go faster.
        player.reset_start()
        car_manager.accelerate()
        # the scoreboard tally goes up by 1
        scoreboard.level_up()
    for vehicle in car_manager.traffic:
        # if a collision occurs with any of the vehicles, the game ends. The values here are what 'seem' to work best.
        if 19 > vehicle.ycor() - player.ycor() > -19 and 24 > vehicle.xcor() - player.xcor() > -24:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
