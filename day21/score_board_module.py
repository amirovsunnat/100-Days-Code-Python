from turtle import Turtle


class ScoreBoard(Turtle):
    """ScoreBoard class"""
    def __init__(self):
        self.r_score = 0
        self.l_score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.refresh()

    def refresh(self):
        """Updates score"""
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}",
                   move=False, align='Center', font=('Courier', 55, 'bold'))

    def right_scores(self):
        self.r_score += 1
        self.refresh()

    def left_scores(self):
        self.l_score += 1
        self.refresh()
