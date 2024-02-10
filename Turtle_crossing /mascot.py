from turtle import Turtle

UP = 90
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class Mascot(Turtle):
    def __init__(self):
        super().__init__()
        self.create_mascot()

    def create_mascot(self):
        self.shape('turtle')
        self.penup()
        self.goto(x=0, y=-320)
        self.setheading(UP)
        self.color('black')

    def go(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def turn_left(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

    def turn_right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
