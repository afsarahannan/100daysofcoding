from turtle import *
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

turtle_bet = screen.textinput(title="Make your bet",
                              prompt="Which turtle do you bet on? \nSet a color from \n(red/ blue/ green/ orange/ yellow/ purple)")


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    new_turtle.color(colors[i])
    all_turtle.append(new_turtle)

if turtle_bet:
    is_race_on = True
else:
    print("You did not place a bet, son!")

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_turtle = turtle.pencolor()
            if win_turtle == turtle_bet:
                write(f"Hurray, {win_turtle} turtle has won the race", align = "center", font = ("Cooper Black", 15, 'italic'))
            else:
                write(f"Sorry your turtle lost :'( {win_turtle} is the winner.", align = "center", font = ("Cooper Black", 15, 'italic'))

        else:
            turtle.forward(random.randint(0, 10))


screen.exitonclick()


