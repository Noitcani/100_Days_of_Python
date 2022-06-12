from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.speed_boost = 1
        self.bounce_x_direction = 1
        self.bounce_y_direction = 1

    def spawn_ball(self):
        self.ht()
        self.home()
        self.st()
        self.speed_boost = 1
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])

    def move(self):

        new_x = self.xcor() + (self.x_move * self.speed_boost)
        new_y = self.ycor() + (self.y_move * self.speed_boost)
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.speed_boost += 0.1


