from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating screen
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)
# creating separating line
line = Turtle()
line.goto(0, 300)
line.color("white")
line.setheading(270)
# drawing dotted line
while line.ycor() > -300:
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

# creating two paddles
r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)
# control settings - right paddle is controlled by up, down, left one - W,S
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
# creating a ball
ball=Ball()
# creating a scoreboard
score=Scoreboard()

game_is_on = True
while game_is_on:
    score.update_scoreboard()
    # controls speed of the ball
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # bounces if hits the wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()
    # bounces when hits the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_increase()
    # restart if left player misses the ball, adds point to right player
    # identical for right player
    if abs(ball.xcor()) > 380:
        if ball.xcor() > 0:
            score.l_point()
        else:
            score.r_point()
        ball.restart()
        ball.speed_reset()
        ball.bounce_x()
        ball.bounce_y()


screen.exitonclick()
