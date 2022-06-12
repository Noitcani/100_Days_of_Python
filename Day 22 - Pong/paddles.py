from turtle import Turtle
import time

MOVE_DIST = 40


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.pu()
        self.pensize(8)
        self.player = player
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.ht()
        self.spawn_paddle(player)
        self.st()
        self.moving_up = False
        self.moving_down = False

    def spawn_paddle(self, player):
        if player == "left_player":
            self.color("Red")
        else:
            self.color("Blue")

        if player == "left_player":
            self.setpos(x=-380, y=0)
        else:
            self.setpos(x=380, y=0)

    def move_up(self):
        if self.ycor() < 200:
            new_ycor = self.ycor() + MOVE_DIST
            self.goto(x=self.xcor(), y=new_ycor)

    def move_down(self):
        if self.ycor() > -200:
            new_ycor = self.ycor() - MOVE_DIST
            self.goto(x=self.xcor(), y=new_ycor)






