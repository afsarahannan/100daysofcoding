from turtle import Turtle

MOVE_DISTANCE = 40


class Paddle(Turtle):
    def __init__(self,
                 positions=None):
        super().__init__()
        self.create_paddle(positions)

    def create_paddle(self, positions):
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(positions)

    def up(self):
        if self.ycor() < 250 - MOVE_DISTANCE:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -200 - MOVE_DISTANCE:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
