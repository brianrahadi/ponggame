from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(position)
        self.setheading(90)
        self.turtlesize(1, 5)
        

    def up(self):
        self.fd(40)

    def down(self):
        self.bk(40)