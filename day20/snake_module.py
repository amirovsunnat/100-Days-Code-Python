from turtle import Turtle, Screen


screen = Screen()
SNAKE_MOVEMENT = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class"""
    def __init__(self):
        self.snake_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        """Creating snake"""
        for position in self.snake_positions:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        """Move snake"""
        for pos in range((len(self.snakes) - 1), 0, -1):
            x_cor = self.snakes[pos - 1].xcor()
            y_cor = self.snakes[pos - 1].ycor()
            self.snakes[pos].goto(x_cor, y_cor)
        self.snakes[0].forward(SNAKE_MOVEMENT)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:

            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
