from turtle import Turtle

FONT = ("Courier", 80, "bold")
END_FONT = ("Courier", 35, "bold")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto((position))
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=FONT)

    def gameover(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(f"{winner} side wins the game!", align="center", font=FONT)