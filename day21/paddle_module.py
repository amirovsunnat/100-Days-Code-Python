from turtle import Turtle


class Paddle(Turtle):
    """Paddle class inherits from Turtle"""
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.8, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



