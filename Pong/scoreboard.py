from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self, player=None, position=None):
        super().__init__()
        self.player = player
        self.position = position
        self.lives = 3
        self.create_scoreboard()

    def create_scoreboard(self):
        self.setposition(self.position)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard(self.player)

    def update_scoreboard(self, player):
        self.write(f'{player}: {self.lives}', move=False, align=ALIGNMENT, font=FONT)

    def decrease_lives(self):
        self.clear()
        self.lives -= 1
        self.update_scoreboard(self.player)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"{self.player} lost the game", move=False, align=ALIGNMENT, font=FONT)


