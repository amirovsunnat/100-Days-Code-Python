import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
t.colormode(255)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen", "blue", "lime", "red", "gold", "snow", "dark violet", "dark orange", "dark slate blue",
#            "light sky blue", "black", "dodger blue", "gainsboro", "yellow", "dark olive green"]


def random_color():
    """Generate random rgb color, and returns it"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


my_turtle.speed('normal')
my_turtle.width(7)

for i in range(500):
    way = random.choice([0, 90, 180, 270])
    my_turtle.forward(20)
    my_turtle.setheading(way)
    my_turtle.color(random_color())


screen = t.Screen()
screen.exitonclick()

