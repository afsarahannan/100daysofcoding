from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Pong Master 2000")
screen.tracer(0)

# the partition in the middle
dashed_line = Turtle('square')
dashed_line.goto(x=0, y=-280)
dashed_line.setheading(90)
dashed_line.color('white')
dashed_line.width(5)

for _ in range(19):
    dashed_line.forward(20)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()

dashed_line.hideturtle()

paddle1 = Paddle()
paddle2 = Paddle()
score = Scoreboard()

start_game = screen.textinput(title="Are you ready for an epic game of PONG!",
                              prompt="Enter 's' to begin.")


def screen_control():
    screen.listen()
    screen.onkey(paddle1.up, 'Up')
    screen.onkey(paddle1.down, 'Down')

    screen.onkey(paddle2.up, 'w')
    screen.onkey(paddle2.down, 's')


if start_game == 's':
    game_is_on = True
else:
    game_is_on = False

# while game_is_on:
screen_control()
screen.update()
time.sleep(0.1)
paddle1.move()
paddle2.move()

screen.exitonclick()
