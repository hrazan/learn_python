import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard

is_game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)

screen.listen()
snake = Snake()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

food = Food()
score_board = ScoreBoard(screen.window_height() / 2)
# score_board.update_score(score)

while is_game_on:
    screen.update()
    time.sleep(0.1/snake.speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.score += 1
        snake.increase_body()
        snake.speed += 0.01
        score_board.update_score()
        # print("NOMNOM")
    else:
        print(snake.body_position())
        print(snake.head.pos())
        if snake.head.pos() in snake.body_position():
            print("body struck!")
            is_game_on = False
        elif (abs(snake.head.pos()[0] * 2) >= screen.window_width()) or (abs(snake.head.pos()[1] * 2) >= screen.window_height()):
            print("window struck")
            is_game_on = False

screen.exitonclick()