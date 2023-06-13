from turtle import Turtle


class ScoreBoard(Turtle):
    """ScoreBoard class for keeping track of score."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        with open("data.txt", mode="r") as f:
            highest_score = f.read()
        self.write(f'Score: {self.score}, Highest Score: {highest_score}',
                   move=False, align='Center', font=('Verdana', 22, 'bold'))

    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER',
    #                move=False, align='Center', font=('Verdana', 25, 'bold'))







