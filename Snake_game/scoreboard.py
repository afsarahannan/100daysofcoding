from turtle import Turtle
import random
from typing import TextIO

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    # def game_over_sign(self):
    #     self.setposition(0, 0)
    #     self.write("Game Over.", move=False, align=ALIGNMENT, font=FONT)

