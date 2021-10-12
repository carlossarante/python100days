from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        self.player_won = False
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.left(90)

    def move_up(self):
        next_y = self.ycor() + 20

        if next_y < 280:
            self.sety(next_y)
        if next_y > 240:
            self.player_won = True

    def move_down(self):
        next_y = self.ycor() - 20

        if next_y >= -280:
            self.sety(next_y)

    def restart_turtle(self):
        self.player_won = False
        self.setposition(STARTING_POSITION)

