import turtle as t

my_turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def turn_left():
    new_left_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_left_heading)

    # my_turtle.left(10)


def turn_right():
    new_right_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_right_heading)

    # my_turtle.right(10)


def clean_screen():
    my_turtle.clear()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clean_screen, key="c")

screen.exitonclick()
