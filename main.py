from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()

# Create Window
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Instantiate Classes
snake = Snake()
food = Food()
score = Score()

# Key instructions
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Move Snake
difficulty = []
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    limit_wall = 295
    if snake.head.xcor() > limit_wall \
            or snake.head.ycor() > limit_wall \
            or snake.head.xcor() < -limit_wall \
            or snake.head.ycor() < -limit_wall:
        score.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False






screen.exitonclick()
