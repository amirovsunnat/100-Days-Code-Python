from turtle import Screen
import time

from paddle_module import Paddle
from ball_module import Ball
from score_board_module import ScoreBoard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game !")
screen.tracer(0)

right_paddle = Paddle(450, 0)
left_paddle = Paddle(-450, 0)

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.04)
    screen.update()
    ball.move_ball()

    # collision with up and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 420 or \
            ball.distance(left_paddle) < 60 and ball.xcor() < -420:
        ball.bounce_x()

    # right paddle miss the ball
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.left_scores()

    # left paddle miss the ball
    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.right_scores()

screen.exitonclick()
