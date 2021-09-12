import random
import turtle
from turtle import Turtle, Screen, colormode
import heroes
from random import randint
from dotter import horizontal_line_dotter

#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

dot_size = 5
size = 0

def set_random_color(turtle_instance):
    colormode(255)
    turtle_instance.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

# def draw_shape(shape_sides):
#     set_random_color(timmy_the_turtle)
#     angle = 360 / shape_sides
#     print(angle)
#
#     for _ in range(0, shape_sides):
#         timmy_the_turtle.forward(50)
#         timmy_the_turtle.right(angle)

# def random_walk(steps):
#     color_list = ['orchid', 'teal', 'navy', 'red']
#     directions = [0, 90, 180, 270]
#     random_angle = 90
#     timmy_the_turtle.pensize(5)
#
#     for _ in range(0, steps + 1):
#         timmy_the_turtle.color(random.choice(color_list))
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.setheading(random.choice(directions))
#
#     timmy_the_turtle.pensize(0)

def draw_spirograph(divider = 5):
    current_angle = 0
    turtle.speed(20)

    for i in range(0, int(360 / divider)):
        current_angle = current_angle + divider
        turtle.circle(100)
        turtle.setheading(turtle.heading() + divider)
        set_random_color(turtle)


if __name__ == '__main__':
    pen = Turtle()
    pen.hideturtle()
    pen.backward(100)
    pen.penup()
    for _ in range(1, 11):
        horizontal_line_dotter(pen)


screen = Screen()
screen.exitonclick()
