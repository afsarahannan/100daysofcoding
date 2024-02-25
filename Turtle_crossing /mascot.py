from turtle import Turtle

UP = 90
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
STARTING_POSITION = (0, -320)
MOVE_INCREMENT = 10


class Mascot(Turtle):
    def __init__(self):
        super().__init__()
        self.create_mascot()
        self.move_distance = MOVE_DISTANCE
        self.go_to_start()

    def create_mascot(self):
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.color('black')

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def go(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def turn_left(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

    def turn_right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
