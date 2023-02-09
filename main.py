import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manage = CarManager()
scoreboard = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manage.create_car()
    car_manage.move_cars()

    # detect collision with cars
    for car in car_manage.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # detect successfull crossing
    if player.is_at_finish_line():
        car_manage.level_up()
        scoreboard.increment_level()
        player.go_to_start()



screen.exitonclick()
