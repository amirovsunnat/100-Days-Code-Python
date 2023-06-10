from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.color("blue")
        self.write(f"  GAME OVER.\n\nTotal score: {self.score}.", move=False, align="Left", font=FONT)
