from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.hideturtle()
        self.get_high_score_from_db()
        self.update_scoreboard()

    def get_high_score_from_db(self):
        with open("score_database.txt", mode="r") as file:
            try:
                self.high_score = int(file.readline())
            except ValueError as e:
                self.score = 0
                self.high_score = 0
                self.store_high_score_in_db(self.high_score)

    def store_high_score_in_db(self, high_score):
        with open('score_database.txt', mode="w") as file:
            file.write(str(high_score))


    def update_scoreboard(self):
        self.write(f"High Score {self.high_score} | Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.color('white')
        if self.high_score < self.score:
            self.high_score = self.score
            self.store_high_score_in_db(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def permanent_store(self, score):
        with open('score_database.txt', mode="a") as file:
            file.write(score)
