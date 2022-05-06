from turtle import Turtle, Screen
import time
from paddle import Paddle
from baal import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0), color="blue")
l_paddle = Paddle((-350, 0), color="red")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle

    if ball.distance(r_paddle) < 60 and ball.xcor() > 325 or ball.distance(l_paddle) < 60 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
