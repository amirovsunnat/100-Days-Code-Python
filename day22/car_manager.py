from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def car_create(self):
        random_num = random.randint(1, 10)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.penup()
            car.setheading(180)
            random_position = (290, random.randint(-260, 260))
            car.goto(random_position)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

