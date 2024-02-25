from turtle import Turtle
import random

UP = 90
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'cyan', 'violet']

class Car:

    def __init__(self):
        self.all_cars = []
        self.move_distance = MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=1.5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(LEFT)
            random_y = random.randint(-250, 290)
            new_car.goto(x=450, y=random_y)
            self.all_cars.append(new_car)

    def cars_move(self):
        for cars in self.all_cars:
            cars.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT