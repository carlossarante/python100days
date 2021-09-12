import turtle
from turtle import Turtle, colormode
from random import randint

def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def horizontal_line_dotter(turtle_instance, distance=100, divider=10):
    gap = distance / divider
    cursor = 0
    colormode(255)
    turtle_instance.penup()

    while cursor < distance:
        turtle_instance.color(get_random_color())
        turtle_instance.dot(10)
        turtle_instance.forward(divider + gap)
        cursor += divider

    turtle_instance.setheading(90)
    turtle_instance.forward(gap * 2)
    turtle_instance.setheading(turtle_instance.heading() - 90)
    turtle_instance.backward(200)
