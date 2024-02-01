from turtle import Turtle


paddle1_position = [(-280, 240), (-280, 220), (-280, 200)]
paddle2_position = [(280, 240), (280, 220), (280, 200)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle(paddle1_position)
        self.create_paddle(paddle2_position)
        self.head = self.segments[0]

    def create_paddle(self, paddle_positions):
        for position in paddle_positions:
            self.add_segments(position)

    def add_segments(self, position):
        paddle = Turtle('square')
        paddle.color('white')
        paddle.penup()
        paddle.goto(position)
        self.segments.append(paddle)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.setheading(90)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)
    def down(self):
        self.head.setheading(DOWN)

