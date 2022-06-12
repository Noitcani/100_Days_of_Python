from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.starting_snake()
        self.length = len(self.snake_body)
        self.head = self.snake_body[0]

    def grow(self, x_appear, y_appear):
        new_part = Turtle(shape="square", visible=False)
        new_part.pu()
        new_part.setpos(x=x_appear, y=y_appear)
        new_part.color("white")
        new_part.st()
        self.snake_body.append(new_part)
        self.length = len(self.snake_body)

    def starting_snake(self):
        # Starting snake
        starting_head_x = 0
        starting_head_y = 0
        for i in range(3):
            self.grow(starting_head_x, starting_head_y)
            starting_head_x -= 20

    def snake_move(self):
        for i in range(self.length - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def turn_left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def turn_down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def turn_right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
