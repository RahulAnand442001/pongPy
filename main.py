import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('PONG')
screen.delay(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_Game_On = True

while is_Game_On:
    time.sleep(ball.move_speed)
    ball.move_ball()
    # detecting collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounceY()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
