from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The snake game")
# this will turn off the screen update
# till until the whole snake body appears
screen.tracer(0)

# creating the snake body in 3 parts
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # the screen.update() will make the snake body move together without time lag
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
