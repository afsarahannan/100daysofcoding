from turtle import Turtle, Screen
from mascot import Mascot
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.title("Timmy crosses the road")
screen.bgcolor("white")
screen.tracer(0)

timmy=Mascot()

def screen_control():
    screen.listen()
    screen.onkey(timmy.go, 'Up')
    screen.onkey(timmy.turn_left, "Left")
    screen.onkey(timmy.turn_right, 'Right')



screen_control()
screen.update()
time.sleep(0.01)

screen.exitonclick()


