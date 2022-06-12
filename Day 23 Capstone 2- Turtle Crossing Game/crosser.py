from turtle import Turtle

START_POS = (0, -280)


# Make a Turtle class/object
class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(START_POS)
        self.setheading(90)
        self.shape("turtle")
        self.fillcolor("green")
        self.pencolor("black")
        self.st()

    # die/respawn (). Reset to start
    def spawn(self):
        self.ht()
        self.goto(START_POS)
        self.setheading(90)
        self.st()

    # move() Allow Turtle to move
    def move_fd(self):
        self.setheading(90)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        if self.xcor() > -265:
            self.forward(20)

    def move_right(self):
        self.setheading(0)
        if self.xcor() < 265:
            self.forward(20)

    def move_down(self):
        self.setheading(270)
        if self.ycor() > -280:
            self.forward(20)
