from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.color('white')
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGNMENT, font=FONT)
