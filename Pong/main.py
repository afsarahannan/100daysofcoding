from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Master 2000")
screen.tracer(0)

# the partition in the middle
dashed_line = Turtle('square')
dashed_line.goto(x=-10, y=-280)
dashed_line.setheading(90)
dashed_line.color('white')
dashed_line.width(5)

for _ in range(19):
    dashed_line.forward(20)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()

dashed_line.hideturtle()


start_game = screen.textinput(title="Are you ready for an epic game of PONG!",
                              prompt="Enter 's' to begin.")

p1 = Paddle((370, 0), 'lightblue')
p2 = Paddle((-370, 0), 'pink')
p1_score = Scoreboard(player='p1', position=(140, 270))
p2_score = Scoreboard(player='p2', position=(-150, 270))
ball = Ball()

def screen_control():
    screen.listen()
    screen.onkey(p1.up, 'Up')
    screen.onkey(p1.down, 'Down')

    screen.onkey(p2.up, 'w')
    screen.onkey(p2.down, 's')

# Ask the user if they want to play the game

if start_game == 's':
    game_is_on = True
else:
    game_is_on = False

while game_is_on:
    screen_control()
    screen.update()
    time.sleep(ball.move_speed)

    ball.move_around()

# bouncing off the walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

# bouncing off the paddles
    if ball.distance(p1) < 30 and ball.xcor() > 260 or ball.distance(p2) < 30 and ball.xcor() < -320:
        ball.paddle_bounce()

    # decreasing score for the player 1
    if ball.xcor() >= 390:
        time.sleep(2)
        ball.reset_position()
        p1_score.decrease_lives()

    if ball.xcor() <= -390:
        time.sleep(2)
        ball.reset_position()
        p2_score.decrease_lives()


# Game over
    if p1_score.lives == 0:
        p1_score.game_over()
        game_is_on = False

    if p2_score.lives == 0:
        p2_score.game_over()
        game_is_on = False


screen.exitonclick()
