from turtle import Turtle, Screen

#Create an object of the Turtle and Screen class
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#to listen to the screen events
#Note: When we pass a function as an input to another function,
#we do not use the parenthesis for the inner function.

screen.listen()
screen.onkey(key = "w", fun=move_forward)
screen.onkey(key = 's', fun=move_backward)
screen.onkey(key = 'a', fun=counter_clockwise)
screen.onkey(key = 'd', fun=clockwise)
screen.onkey(key = 'c', fun=clear_screen)

screen.exitonclick()
