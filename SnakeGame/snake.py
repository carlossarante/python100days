from turtle import Turtle

RIGHT_DIRECTION = 0
UP_DIRECTION = 90
LEFT_DIRECTION = 180
DOWN_DIRECTION = 270

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_instance(self, offset):
        turtle_instance = Turtle()
        turtle_instance.penup()
        turtle_instance.color("green")
        turtle_instance.shape("square")
        turtle_instance.goto(offset)

        return turtle_instance

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def grow(self):
        offset = self.squares[-1].position()
        turtle_instance = self.create_instance(offset)
        self.squares.append(turtle_instance)

    def create_snake(self):
        offset = [(0, 0), (0, -20), (0, -40)]

        for turtle in range(0, 3):
            turtle_instance = self.create_instance(offset[turtle])

            self.squares.append(turtle_instance)

    def move(self):
        for seg_index in range(len(self.squares) - 1, 0, -1):  # start=length of snake - 1, stop=0, counter = -1
            new_x = self.squares[seg_index - 1].xcor()
            new_y = self.squares[seg_index - 1].ycor()
            self.squares[seg_index].goto((new_x, new_y))

        self.head.forward(20)

    def up(self):
        if self.squares[0].heading() != DOWN_DIRECTION:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(0)
