from turtle import Turtle
import random

UP = 90
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 1
COLORS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'cyan', 'violet']
# LOCATION = [-290, 300]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()
        self.cars_move()
        self.car_speed = 0.01

    def create_cars(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(LEFT)
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.goto(x=random.randint(-450, 450), y=random.randint(-290, 290))

    def cars_move(self):
        self.forward(MOVE_DISTANCE)
