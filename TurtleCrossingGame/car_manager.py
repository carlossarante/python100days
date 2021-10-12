import time
from random import choice, randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_PER_GROUP = 6


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.color(choice(COLORS))
        self.left(90)
        self.sety(randint(-240, 240))
        self.setx(randint(300, 400))

    def run(self):
        self.setx(self.xcor() - 20)

    def has_crashed(self, turtle):
        distance = self.distance(turtle)
        return distance <= 20



class CarManager:
    def __init__(self, player):
        super().__init__()
        self.current_cars = []
        self.player = player

    def create_cars(self):
        self.current_cars.append(Car())
