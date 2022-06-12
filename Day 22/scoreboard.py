from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("white")
        self.goto(x=0, y=180)
        self.left_score = 0
        self.right_score = 0
        self.write(f"{self.left_score}         {self.right_score}", align="center", font=("impact", 30, "normal"))

    def scored(self, player):
        self.clear()
        if player == "left_player":
            self.left_score += 1
            self.write(f"{self.left_score}         {self.right_score}", align="center", font=("impact", 30, "normal"))
        else:
            self.right_score += 1
            self.write(f"{self.left_score}         {self.right_score}", align="center", font=("impact", 30, "normal"))

    def game_over(self, player):
        self.goto(x=0, y=10)
        self.write(f"Game Over. {player} wins!", align="center", font=("impact", 30, "normal"))



