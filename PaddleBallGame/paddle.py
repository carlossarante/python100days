from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.setposition(start_x, start_y)
        self.shape("square")
        self.color("white")
        self.color(PADDLE_COLOR)
        self.penup()
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)
        self.getscreen().update()
        self.ceiling = self.getscreen().window_height() / 2 - (PADDLE_HEIGHT / 2 * 20)
        self.floor = -self.getscreen().window_height() / 2 + (PADDLE_HEIGHT / 2 * 20) + 10

    def go_up(self):
        new_y = self.ycor() + 10
        if new_y < self.ceiling:
            self.goto(self.xcor(), new_y)
            self.getscreen().update()

    def go_down(self):
        new_y = self.ycor() - 10
        if new_y > self.floor:
            self.goto(self.xcor(), new_y)
            self.getscreen().update()

    def set_keys(self, up, down):
        self.getscreen().onkeypress(self.go_up, up)
        self.getscreen().onkeypress(self.go_down, down)
