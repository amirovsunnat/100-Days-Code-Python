import random
import turtle as t

import colorgram

# colors = colorgram.extract("painting.jpg", 45)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

colors_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
               (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
               (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
               (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
               (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]
my_turtle = t.Turtle()
t.colormode(255)
my_turtle.penup()  # to remove the line

my_turtle.setheading(210)
my_turtle.forward(330)
my_turtle.setheading(0)
total_dots = 100

for dot in range(1, total_dots + 1):
    my_turtle.dot(20, random.choice(colors_list))
    my_turtle.forward(50)

    if dot % 10 == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(500)
        my_turtle.setheading(0)
my_turtle.hideturtle()  # to hide turtle


screen = t.Screen()
screen.exitonclick()



