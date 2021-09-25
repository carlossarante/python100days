from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(-90, 200)
        self.write(self.left_score, font=("Courier", 80, "normal"))
        self.goto(25, 200)
        self.write(self.right_score, font=("Courier", 80, "normal"))
        self.getscreen().update()

    def update_scoreboard(self):
        self.clear()
        self.goto(-90, 200)
        self.write(self.left_score, font=("Courier", 80, "normal"))
        self.goto(25, 200)
        self.write(self.right_score, font=("Courier", 80, "normal"))

    def increment_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increment_right_score(self):
        self.right_score += 1
        self.update_scoreboard()
