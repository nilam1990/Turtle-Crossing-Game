from turtle import Turtle
import random
COLORS = ["red", "orange", "blue",  "purple", "green", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        no_of_car = random.randint(1, 6)
        if no_of_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(250, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
