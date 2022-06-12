import time

from turtle import Screen
from midline import draw_midline
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard

game_on = True

# Make screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=500, width=800)
screen.title("Pong!")
screen.textinput("Welcome to Pong!",
                 '''
                 Left Player (RED): Up = W, Down = S
                 Right Player (BLUE): Up = Up arrow, Down = Down arrow
                 Type any key to start!
                 ''')
# Draw midline

screen.tracer(0)
draw_midline()

ball = Ball()

left_paddle = Paddle("left_player")
screen.listen()
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")

right_paddle = Paddle("right_player")
screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")

scoreboard = Scoreboard()

while game_on:
    screen.update()

    ball.move()
    if (ball.ycor() >= 230 and ball.y_move > 0) or (ball.ycor() <= -230 and ball.y_move < 0):
        ball.bounce_wall()

    if (ball.distance(left_paddle) < 60 and ball.xcor() <= -360 and ball.x_move < 0)\
            or (ball.distance(right_paddle) < 60 and ball.xcor() >= 360 and ball.x_move > 0):
        ball.bounce_paddle()

    if ball.xcor() <= -400:
        scoreboard.scored("right_player")
        ball.spawn_ball()

    if ball.xcor() >= 400:
        scoreboard.scored("left_player")
        ball.spawn_ball()

    if scoreboard.left_score == 5:
        scoreboard.game_over("Left Player")
        game_on = False

    if scoreboard.right_score == 5:
        scoreboard.game_over("Right Player")
        game_on = False

    time.sleep(0.02)

    # if ball.distance(test) < 50:
    #     ball.setheading(360-ball.towards(test))
    # time.sleep(0.05)

screen.exitonclick()
