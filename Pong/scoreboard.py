from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
POSITIONS = [(-150, 270), (140, 270)]
PLAYERS = ['P1', 'P2']


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.create_scoreboard()

    def create_scoreboard(self):
        for i in range(0, len(POSITIONS)):
            self.setposition(POSITIONS[i])
            self.color('white')
            self.penup()
            self.hideturtle()
            self.update_scoreboard(PLAYERS[i])

    def update_scoreboard(self, player):
        self.write(f'{player}: {self.lives}', move=False, align=ALIGNMENT, font=FONT)

    def decrease_lives_p1(self):
        self.clear()
        self.lives -= 1
        self.update_scoreboard(PLAYERS[0])

    def decrease_lives_p2(self):
        self.clear()
        self.lives -= 1
        self.update_scoreboard(PLAYERS[1])

