import turtle
from turtle import Screen
import snake
import time
import food
import scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Nokia Snake")
# disabling auto screen updates:
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

sleep_time = 0.2

game_on = True
while game_on:
    screen.update()
    time.sleep(sleep_time)

    snake.snake_movement()

    # Detect snake movement
    if snake.snake_segments[0].distance(food) <= 15:
        food.refresh()
        scoreboard.score += 1
        snake.extend()
        sleep_time -= 0.01
    scoreboard.scoreboard_display()

    # Detect collision with wall:
    if snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].xcor() < -280 or snake.snake_segments[
        0].ycor() > 280 or snake.snake_segments[0].ycor() < -280:
        scoreboard.reset()
        snake.snake_reset()

    # detect collision with tail:
    for segment in snake.snake_segments[1:]:
        # if segment == snake.snake_segments[0]:
        #     pass
        if snake.snake_segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.snake_reset()

screen.exitonclick()
