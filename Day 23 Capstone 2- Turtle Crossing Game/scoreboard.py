from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.setpos(x=-260, y=280)

    def display_level(self, level):
        self.clear()
        self.write(f"Current level: {level}", align="left", font=("Impact", 13, "normal"))

    def game_over(self):
        self.setpos(x=0, y=0)
        self.write("Game Over!", align="center", font=("Impact", 13, "normal"))
