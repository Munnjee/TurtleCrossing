import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Set up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects
turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Turtle Movement
screen.listen()
screen.onkey(turtle.move_up, 'Up')
screen.onkey(turtle.move_down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create Random Cars on Screen
    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with Car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if turtle.finish_line():
        turtle.goto_start()
        car_manager.level_up()
        scoreboard.next_level()

screen.exitonclick()
