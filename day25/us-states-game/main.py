from turtle import Turtle, Screen
import pandas


my_turtle = Turtle()
screen = Screen()
screen.title("US States")
states_image = "blank_states_img.gif"
screen.addshape(states_image)
my_turtle.shape(states_image)

# pandas
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].tolist()


not_finished = True
right_answer = 0
founded_states = []
while not_finished:
    user_guess = screen.textinput(title=f" {right_answer}/50 States Correct", prompt="What's another state name?").title()

    if user_guess.strip() == "Exit":
        not_finished = False

    for state in states_names:
        if user_guess.strip() == state and user_guess.strip() not in founded_states:
            state_info = states_data[states_data["state"] == state]
            state_x_pos = int(state_info.x)
            state_y_pos = int(state_info.y)
            my_next_turtle = Turtle()
            my_next_turtle.penup()
            my_next_turtle.hideturtle()
            my_next_turtle.goto(state_x_pos, state_y_pos)
            my_next_turtle.color("blue")
            my_next_turtle.write(f"{user_guess.strip()}", align="center",  font=("Verdana", 6, "bold"))
            right_answer += 1
            founded_states.append(state)

# comprehension style is used to check learning states
need_to_learn_states = [s for s in states_names if s not in founded_states]

states = pandas.DataFrame(need_to_learn_states)
states.to_csv("need_to_learn_states.csv")
