import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = t.Screen()
screen.exitonclick()

