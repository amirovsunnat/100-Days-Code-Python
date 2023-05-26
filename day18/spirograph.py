import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
t.colormode(255)
my_turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_circles(space_between_circle):
    """Takes only one input to specify space between circles, and returns spirograph"""
    for i in range(360//space_between_circle):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + space_between_circle)
        my_turtle.circle(100)


draw_circles(4)

screen = t.Screen()
screen.exitonclick()

