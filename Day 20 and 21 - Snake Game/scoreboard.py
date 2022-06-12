from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.pencolor("white")
        self.score = 0
        self.setpos(x=0, y=280)
        self.write(arg=f"Current Score: {self.score}", align="center", font=('Arial', 13, 'normal'))

    def refresh(self):
        self.clear()
        self.write(arg=f"Current Score: {self.score}", align="center", font=('Arial', 13, 'normal'))

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg=f"Game Over", align="center", font=('Arial', 15, 'normal'))



