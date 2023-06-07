# let's create turtle race game
import random
import turtle as t

colors = ["red", "blue", "yellow", "green", "orange", "purple"]
screen = t.Screen()
t.setup(width=800, height=600)
user_guess = t.textinput(title="First turtle", prompt="Which color of turtle you think will come first: ").lower() # taking user guess
y_position = -200  # for setting turtles positions
b = 0  # for looping through colors
is_game_on = False
total_turtles = []

for turtle in range(6):
    turtle = t.Turtle("turtle")
    turtle.penup()  # we need to penup() function because we don't need to draw the screen
    turtle.color(colors[b])
    turtle.goto(x=-500, y=y_position)  # simple bug we should use -385 instead of 385
    y_position += 70
    b += 1
    total_turtles.append(turtle)  # adding new turtles to overall turtle list

if user_guess:
    is_game_on = True

while is_game_on:
    for turtle in total_turtles:
        if turtle.xcor() > 780:
            is_game_on = False
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_guess:
                print(f"You've won. The {winning_turtle_color} turtle came first")
            else:
                print(f"You've lost. The {winning_turtle_color} turtle came first")

        random_distanse = random.randint(1, 10) # every turtle go forwards in random distanse
        turtle.forward(random_distanse)

        turtle.clear()
screen.exitonclick()
