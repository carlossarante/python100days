from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

turtle = ""
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake from Nokia")
screen.tracer(0)
snake = Snake()
food = Food()
is_game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
scoreboard = ScoreBoard()

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect distance

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    #detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print(f'Failed on {snake.head.position()}')

        is_game_on = False
        scoreboard.game_over()

    for segment in snake.squares[1:]:
        if snake.head.distance(segment) < 10:
            print(f'Failed on {snake.head.position()} -> {segment.position()}')
            is_game_on = False
            scoreboard.game_over()






screen.exitonclick()
