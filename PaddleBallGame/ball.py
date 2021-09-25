from turtle import Turtle

DELTA = 10


class Ball(Turtle):
    def __init__(self, paddle_left_x, paddle_right_x):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.paddle_left_x = paddle_left_x
        self.paddle_right_x = paddle_right_x
        self.setposition(0, 0)
        self.x_delta = DELTA / 2
        self.y_delta = DELTA


    def reset_position(self):
        self.goto(0, 0)
        self.x_delta *= -1
        self.y_delta *= -1

    def move(self):
        new_x = self.xcor() + self.x_delta
        new_y = self.ycor() + self.y_delta

        self.setposition(new_x, new_y)
        self.getscreen().update()

    def bounce_down(self):
        self.y_delta = -DELTA

    def bounce_up(self):
        self.y_delta = DELTA

    def bounce_right(self):
        self.x_delta = DELTA

    def bounce_left(self):
        self.x_delta = -DELTA

