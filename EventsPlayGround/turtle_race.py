import turtle
import random
from turtle import Turtle, Screen

def get_turtle_race(screen_width, screen_height, turtle_colors):
    starting_point_x = - screen_width / 2 + 20
    gap = screen_height / len(turtle_colors)
    turtle_list = []
    turtle_y_positions = [-(screen_height / ) + gap * color_index for color_index in range(0, len(turtle_colors))]

    for turtle_index in range(0, len(turtle_colors)):
        turtle_created = Turtle(shape="turtle")
        turtle_created.penup()
        turtle_created.color(turtle_colors[turtle_index])
        turtle_created.goto((starting_point_x, turtle_y_positions[turtle_index]))
        turtle_list.append(turtle_created)

    return turtle_list

def start_race(screen_width, screen_height):
    screen = Screen()
    is_race_on = False
    screen.setup(width=screen_width, height=screen_height)
    user_bet = screen.textinput(title="Make your first bet", prompt="Which turtle will win the race? Enter a color: ")
    turtle_colors = ['red', 'pink', 'blue', 'black', 'yellow', 'gray']
    turtle_list = get_turtle_race(screen_width=screen_width, screen_height=screen_height, turtle_colors=turtle_colors)

    if user_bet:
        is_race_on = True
    while is_race_on:
        # turtle size is 40
        for turtle_created in turtle_list:
            if turtle_created.xcor() > screen_width / 2 - (40 / 2):
                is_race_on = False
                winner_color = turtle.pencolor()

                if user_bet.lower() == winner_color:
                    print(f'You\'ve won! turtle {turtle_created.pencolor()} is the winner!')
                else:
                    print(f'You\'ve lost! turtle {turtle_created.pencolor()} is the winner!')

            random_distance = random.randint(0, 10)
            turtle_created.forward(random_distance)

    screen.exitonclick()