import turtle
import random
import colorgram

import tkinter as TK

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("blue")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

screen = turtle.Screen()
# screen.setup(width=600, height=600)

def check_boundaries():
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2

    # Check if turtle is out of bounds
    if abs(timmy.xcor()) > screen_width or abs(timmy.ycor()) > screen_height:
        timmy.penup()
        timmy.goto(0, 0)
        timmy.pendown()

def dashed_line():
    for i in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

# dashed_line()

#draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

def draw_traingle():
    for i in range(3):
        timmy.forward(100)
        timmy.right(120)
def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
def draw_pentagon():
    for i in range(5):
        timmy.forward(100)
        timmy.right(72)
def draw_shapes(sides, size, color):
    timmy.color(color.lower())
    for i in range(sides):
        timmy.forward(size)
        timmy.right(int(360/sides))

colors = ['red', 'orange', 'yellow','green', 'blue', 'purple', 'pink', 'indigo', 'cyan', 'lightgreen', 'turquoise', 'skyblue']

def draw_mutiple_shapes():
    sides = 3
    rotation = len(colors) + sides
    while sides < rotation:
        for color in colors:
            draw_shapes(sides, 100, color)
            sides += 1

#draw_multiple_shapes()

#designing a random walk

# Define functions to move forward, turn right, and turn left
move_forward = lambda: timmy.forward(30)

directions = [0,90,180,270]
random_turn = lambda: timmy.setheading(random.choice(directions))

# Create a list of functions
actions = [move_forward, random_turn]

# Create a loop for the random walk
def random_walk():
    while True:
        timmy.pensize(15)
        timmy.speed(10)
        timmy.color(random_color())
        random_action = random.choice(actions)
        random_action()  # Execute the randomly chosen action
        check_boundaries()

# random_walk()

def walk_in_circles(gap_size):
    for i in range(int(360/gap_size)):
        timmy.pensize(5)
        timmy.speed(10)
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap_size)


walk_in_circles(30)

screen.exitonclick()
