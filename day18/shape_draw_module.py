import turtle as t
from random import choice

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shapes(number_sides):
    for i in range(number_sides):
        angle = 360 / number_sides
        my_turtle.forward(100)
        my_turtle.right(angle)


x = 3
while x <= 15:
    my_turtle.color(choice(colours))
    draw_shapes(x)
    x += 1


screen = t.Screen()
screen.exitonclick()

