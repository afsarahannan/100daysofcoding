from turtle import Turtle
import random

UP = 90
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
COLORS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'cyan', 'violet']
LOCATION = [-280, 300, 320, 340, 360]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()
        self.cars_move()

    def create_cars(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(LEFT)
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.goto(x=400, y=random.choice(LOCATION))

    def cars_move(self):
        self.forward(MOVE_DISTANCE)
