from turtle import Turtle

PADDLE_COLOR = "#ffa62b"
PADDLE_SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.penup()
        self.goto(positions)

    def move_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y=y_position)

    def move_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y=y_position)
