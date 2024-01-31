from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
score = Scoreboard()


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

    # score increase when the snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # game over when snake hits wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.xcor()< -280:
        game_is_on = False
        score.game_over_sign()

    # game over when the snake hits its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(snake.segments) < 10:
            game_is_on = False
            score.game_over_sign()


screen.exitonclick()
