import random
from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "red"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounceY(self):
        self.y_move *= -1

    def bounceX(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounceX()
