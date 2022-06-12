from turtle import Screen
from time import sleep

import cars
from cars import Car
from crosser import Crosser
from scoreboard import Scoreboard


# Set up Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

level = 1
game_on = True

# Crosser and moves
crosser = Crosser()
screen.onkeypress(key="Up", fun=crosser.move_fd)
screen.onkeypress(key="Left", fun=crosser.move_left)
screen.onkeypress(key="Right", fun=crosser.move_right)
screen.onkeypress(key="Down", fun=crosser.move_down)

# Car spawner
car_spawner = Car()
car_spawner.spawner_run(level)

# Scoreboard
scoreboard = Scoreboard()

while game_on:  # game_loop
    screen.update()  # screen_update
    sleep(0.02)

    scoreboard.display_level(level)  # print current_level

    if crosser.ycor() >= 280:  # T collision with top, level up, clear, speed up
        crosser.spawn()
        level += 1
        for car in cars.all_cars:
            car.ht()
            del car
            cars.all_cars = []
        car_spawner.spawner_run(level)

    for car in cars.all_cars:
        for other_cars in cars.all_cars:
            if car.distance(other_cars) < 20 and car != other_cars:
                car.car_respawn(level)
        car.move(level)

    # Respawn car when out of bounds
    for car in cars.all_cars:
        if car.xcor() <= -280:
            car.car_respawn(level)

    # T collision with car, SB: game_over. Press "space" to replay.
    for car in cars.all_cars:
        if crosser.distance(car) < 15:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
