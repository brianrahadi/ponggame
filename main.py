from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_score = Scoreboard((-100, 210))
r_score = Scoreboard((100, 210))
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        l_score.increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        r_score.increase_score()

    if l_score.score == 11:
        game_is_on = False
        l_score.gameover("Left")

    if r_score.score == 11:
        game_is_on = False
        r_score.gameover("Right")


screen.exitonclick()