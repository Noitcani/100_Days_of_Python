from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.setpos(x=random.randint(-280, 280), y=random.randint(-280, 280))
