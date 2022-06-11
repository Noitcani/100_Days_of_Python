from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=my_snake.turn_up, key="Up")
screen.onkey(fun=my_snake.turn_down, key="Down")
screen.onkey(fun=my_snake.turn_left, key="Left")
screen.onkey(fun=my_snake.turn_right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in my_snake.snake_body[1:]:
        if (my_snake.head.distance(seg) < 10):
            game_is_on = False
            my_scoreboard.game_over()

    if my_snake.head.distance(my_food) < 15:
        my_scoreboard.score += 1
        my_snake.grow(x_appear=my_snake.snake_body[-1].xcor(), y_appear=my_snake.snake_body[-1].ycor())
        my_food.refresh()
        my_scoreboard.refresh()

    if (-280 <= my_snake.head.xcor() >= 280) or (-280 <= my_snake.head.ycor() >= 280):
        game_is_on = False
        my_scoreboard.game_over()

    my_snake.snake_move()

screen.exitonclick()
