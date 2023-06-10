import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player_car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player_car.car_create()
    player_car.move_car()

    # collision with cars
    for c in player_car.cars:
        if c.distance(player) < 30:
            game_is_on = False
            screen.clear()
            scoreboard.game_over()

    # is finished
    if player.is_finished():
        scoreboard.increase_score()
        player.start()
        player_car.increase_speed()


screen.exitonclick()






