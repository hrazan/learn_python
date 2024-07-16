import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)
is_game_on = True

screen.listen()
snake = Snake()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

while is_game_on:
    snake.move()
    screen.update()
    time.sleep(0.1/snake.speed)

screen.exitonclick()
