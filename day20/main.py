from turtle import Screen
from snake_module import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game !')
screen.tracer(0)

# create snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    # collision with food
    if snake.snakes[0].distance(food) < 16:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh()

    # collision with wall
    if snake.snakes[0].xcor() > 385 or snake.snakes[0].xcor() < -385 or snake.snakes[0].ycor() > 280 or \
            snake.snakes[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # collision with tail
    for i in snake.snakes[1:]:
        if snake.snakes[0].distance(i) < 5:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()

