from turtle import Turtle, Screen



class ScoreBoard(Turtle):
    """ScoreBoard class for keeping track of score."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        # self.write(f'Score: {self.score}',
        #            move=False, align='Center', font=('Verdana', 14, 'bold'))
        self.refresh()

    def refresh(self):
        """Updates score"""
        self.clear()
        self.write(f'Score: {self.score}',
                   move=False, align='Center', font=('Verdana', 22, 'bold'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER',
                   move=False, align='Center', font=('Verdana', 25, 'bold'))





