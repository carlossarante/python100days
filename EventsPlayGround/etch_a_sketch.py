from turtle import Turtle

class EtchASketch:
    def __init__(self):
        self.pen = Turtle()
        self.current_heading_angle = 0

    def move_forwards(self):
        self.pen.forward(10)

    def move_backwards(self):
        self.pen.backward(10)

    def set_heading_clockwise(self):
        self.current_heading_angle -= 10
        self.pen.setheading(self.current_heading_angle)

    def set_heading_counter_clockwise(self):
        self.current_heading_angle += 10
        self.pen.setheading(self.current_heading_angle)

    def clear_game(self):
        self.current_heading_angle = 0
        self.pen.clear()
        self.pen.reset()

def start_race(turtle_list):
