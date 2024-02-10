import random
from turtle import Screen
from mascot import Mascot
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.setup(width=900, height=700)
screen.title("Timmy crosses the road")
screen.bgcolor("white")
screen.tracer(0)

start_game = screen.textinput(title="Are you ready to help Timmy cross the road",
                              prompt="Enter 's' to begin.")

timmy = Mascot()
score = Scoreboard()
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

    for vehicle in total_cars:
        time.sleep(vehicle.car_speed)

    for vehicle in total_cars:
        vehicle.cars_move()
        vehicle.speed()

    for vehicle in total_cars:
        if vehicle.xcor() < -490:
            vehicle.create_cars()

    if timmy.ycor() > 300:
        score.increase_level()
        timmy.goto(x=0, y=-320)
        for vehicle in total_cars:
            vehicle.car_speed *= 0.09
        print("This works")


    for vehicle in total_cars:
        if timmy.distance(vehicle) < 30:
            score.game_over_sign()
            game_is_on = False


screen.exitonclick()
