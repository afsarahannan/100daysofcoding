from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over_sign(self):
        self.setposition(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def game_pause_sign(self):
        self.setposition(0, 0)
        self.write("The game is paused. Press 's' to start again.", move=False, align=ALIGNMENT, font=FONT)
