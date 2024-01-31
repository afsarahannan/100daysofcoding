# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# turtle.color("coral")
#
# turtle.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

#creating the object
table = PrettyTable()

table.add_column("Pokemon_name", ["Pickachoo", "Squirtle", "Charmander"])
table.align["Pokemon_name"] = "l"
table.padding_width = 5
table.add_column("Type", ["Electric", "Water", "Fire"])



print(table)
