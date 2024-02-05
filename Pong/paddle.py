from turtle import Turtle

paddle_position = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.P1 = self.paddles[0]
        self.P2 = self.paddles[1]

    def create_paddle(self):
        for pos in paddle_position:
            self.add_paddles(pos)

    def add_paddles(self, positions):
        paddle = Turtle('square')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color('white')
        paddle.penup()
        paddle.goto(positions)
        paddle.setheading(180)
        self.paddles.append(paddle)

    def p1_move(self):
        self.P1.forward(MOVE_DISTANCE)

    def p1_up(self):
        self.P1.setheading(UP)

    def p1_down(self):
        self.P1.setheading(DOWN)

    def p2_move(self):
        self.P2.forward(MOVE_DISTANCE)

    def p2_up(self):
        self.P2.setheading(UP)

    def p2_down(self):
        self.P2.setheading(DOWN)
