from turtle import Screen, Turtle
from level import Level
from obstacle import Obstacle
from hero import Hero
import random
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")
screen.title("Tutle Crossing Game")
screen.tracer(0)

hero = Hero(screen.window_height())

screen.listen()
screen.onkey(hero.move_up   , "Up"   )
screen.onkey(hero.move_down , "Down" )
screen.onkey(hero.move_right, "Right")
screen.onkey(hero.move_left , "Left" )

obstacles = []
number_obstacles = 0
summon_time_wait = 0
prev_summon_time = 0
cur_time = 0
level = Level(((-screen.window_width() / 2) + 30, (screen.window_height() / 2) - 50))

is_game_on = True

while is_game_on:
    screen.update()
    level.update_level()
    number_obstacles = level.level
    
    if (len(obstacles) < number_obstacles) and ((time.monotonic_ns() - prev_summon_time) > summon_time_wait):
        obstacles.append(Obstacle(False, screen.window_width(), screen.window_height()))
        prev_summon_time = time.monotonic_ns()
        summon_time_wait = random.randint(1000000, 5000000)

    if len(obstacles) > 0:
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.is_over():
                obstacles.remove(obstacle)

    if hero.ycor() > ((screen.window_height() / 2) - 40):
        level.level += 1
        hero.reset_position()

    


screen.exitonclick()