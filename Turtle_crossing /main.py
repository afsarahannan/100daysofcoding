import random
from turtle import Turtle, Screen
from mascot import Mascot
from car import Car
import time

screen = Screen()
screen.setup(width=900, height=800)
screen.title("Timmy crosses the road")
screen.bgcolor("white")
screen.tracer(0)

start_game = screen.textinput(title="Are you ready to help Timmy cross the road",
                              prompt="Enter 's' to begin.")

timmy = Mascot()
total_cars = []
car_number = random.randint(5, 10)
for _ in range(0, car_number):
    car = Car()
    total_cars.append(car)


def screen_control():
    screen.listen()
    screen.onkey(timmy.go, 'Up')
    screen.onkey(timmy.turn_left, "Left")
    screen.onkey(timmy.turn_right, 'Right')


if start_game == 's':
    game_is_on = True
else:
    game_is_on = False

while game_is_on:

    screen_control()
    screen.update()

    time.sleep(0.9)

    for vehicle in total_cars:
        vehicle.cars_move()

screen.exitonclick()
