import time
import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

THEME_DARK = {
    'bg_color': "black",
    'text_color': 'white'
}

THEME_LIGHT = {
    'bg_color': "white",
    'text_color': 'black'
}


class GameScreen:
    def __init__(self, width=800, height=500, theme='dark'):
        self.screen = Screen()
        self.divider = Turtle()
        self.screen.tracer(0)
        self.speed_counter = 10
        self.screen.setup(width=width, height=height)
        self.set_theme_color(theme)
        self.game_is_on = True
        self.left_paddle = Paddle(-self.screen.window_width() / 2 + 20, 0)
        self.right_paddle = Paddle(self.screen.window_width() / 2 - 25, 0)
        self.ball = Ball(self.left_paddle.xcor(), self.right_paddle.xcor())
        self.scoreboard = ScoreBoard()
        self.ceiling = self.screen.window_height() / 2 + 10
        self.floor = -self.screen.window_height() / 2 + 20
        self.add_divider()
        self.screen.listen()
        self.bind_events()
        self.move_ball()
        self.screen.exitonclick()


    def set_theme_color(self, theme):
        if theme == 'dark':
            self.screen.bgcolor(THEME_DARK['bg_color'])
            self.divider.pencolor(THEME_DARK['text_color'])
        else:
            self.screen.bgcolor(THEME_LIGHT['bg_color'])
            self.divider.pencolor(THEME_LIGHT['text_color'])

    def get_screen_dimensions(self):
        dimension_tuple = (self.screen.window_width(), self.screen.window_height())

        return dimension_tuple

    def add_divider(self):
        current_height = self.screen.window_height() / 2
        self.screen.tracer(0)
        self.divider.penup()
        self.divider.goto(0, current_height)
        self.divider.pensize(2)
        self.divider.setheading(270)
        self.divider.hideturtle()
        self.screen.update()

        while self.divider.ycor() >= -current_height:
            self.divider.pendown()
            self.divider.forward(10)
            self.divider.penup()
            self.divider.forward(5)

    def bind_events(self):
        self.left_paddle.set_keys("w", "s")
        self.right_paddle.set_keys("Up", "Down")

    def move_ball(self):
        while self.game_is_on:
            if self.ceiling == self.ball.ycor() + 10:
                self.ball.bounce_down()
            elif self.floor == self.ball.ycor() :
                self.ball.bounce_up()
            elif self.left_paddle.distance(self.ball) < 30:
                self.ball.bounce_right()
                self.speed_counter += 1

            elif self.right_paddle.distance(self.ball) < 30:
                self.ball.bounce_left()
                self.speed_counter += 1

            elif self.right_paddle.xcor() < self.ball.xcor():
                self.scoreboard.increment_left_score()
                self.ball.reset_position()
                self.speed_counter = 10

            elif self.left_paddle.xcor() > self.ball.xcor():
                self.scoreboard.increment_right_score()
                self.ball.reset_position()
                self.speed_counter = 10

            time.sleep(1 / self.speed_counter)
            self.ball.move()
