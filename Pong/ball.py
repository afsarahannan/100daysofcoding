from turtle import Turtle
import random

RAND_DIRECTION = random.randint(a=0, b=360)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
Y_MOVE = 10
X_MOVE = 10
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink']

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = None
        self.y_move = None
        self.create_ball()
        self.move_speed = 0.06

    def create_ball(self):
        self.setposition(x=0, y=0)
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_around(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.color(random.choice(COLORS))

    def reset_position(self):
        self.home()
        self.color('white')
        self.move_speed = 0.06
        self.paddle_bounce()






