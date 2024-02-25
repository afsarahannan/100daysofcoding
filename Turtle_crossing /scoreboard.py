from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.setposition(-400, 300)
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.penup()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over_sign(self):
        self.penup()
        self.setposition(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
