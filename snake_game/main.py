import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)

body_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_bodies = []

is_game_on = True
snake_speed = 1
snake_direction = 0


def draw_snake():
    for position in body_positions:
        snake_body = Turtle(shape="square")
        snake_body.color((255, 255, 255))
        snake_body.penup()
        snake_body.goto(position)
        snake_bodies.append(snake_body)


def move_snake():
    global snake_direction
    for snake_body in snake_bodies:
        if snake_direction == 0:
            snake_body.forward(20)
        elif snake_direction == 1:
            snake_body.left(90)
    snake_direction = 0


def move_left():
    global snake_direction
    snake_direction = 1


def move_right():
    global snake_direction
    snake_direction = 2


draw_snake()
screen.listen()
screen.onkey(move_left, "space")
screen.onkey(move_right, "Right")

while is_game_on:
    move_snake()
    screen.update()
    time.sleep(0.1/snake_speed)

screen.exitonclick()
