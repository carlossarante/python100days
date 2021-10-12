import time
from turtle import Screen
from Player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score_board = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager(player)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
speed_factor = 2.5

game_is_on = True

while game_is_on:
    car_manager.create_cars()

    for car in car_manager.current_cars:
        car.run()

        if car.has_crashed(player):
            game_is_on = False
            score_board.player_lose()
        elif player.player_won:
            speed_factor += .5
            player.restart_turtle()

    time.sleep(1/speed_factor)
    screen.update()
screen.exitonclick()