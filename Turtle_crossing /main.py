from turtle import Screen, Turtle
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
car_manager = Car()
score = Scoreboard()

#finish line

finish_line = Turtle()
finish_line.penup()
finish_line.goto(-200,300)
finish_line.hideturtle()
finish_line.color('red')
finish_line.width(5)

for _ in range(10):
    finish_line.pendown()
    finish_line.forward(20)
    finish_line.penup()
    finish_line.forward(20)


def screen_control():
    screen.listen()
    screen.onkey(timmy.go, 'Up')
    screen.onkey(timmy.turn_left, "Left")
    screen.onkey(timmy.turn_right, 'Right')


if start_game == 's':
    game_is_on = True
else:
    game_is_on = False


screen_control()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.cars_move()

    for car in car_manager.all_cars:
        if car.distance(timmy) < 15:
            game_is_on = False
            score.game_over_sign()

    if timmy.ycor() == finish_line.ycor():
        score.increase_level()
        timmy.go_to_start()
        car_manager.level_up()
        timmy.level_up()
        print(f'{car_manager.move_distance}')
        print("This works")

screen.exitonclick()
