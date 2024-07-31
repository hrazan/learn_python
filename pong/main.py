from turtle import Screen, Turtle
from paddle import Paddle
from ball   import Ball
from score  import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.colormode(255)
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.color("white")
line.goto(0, -screen.window_height() / 2)
line.goto(0,  screen.window_height() / 2)

p1       = Paddle("red" , ( (screen.window_width() / 2) - 25,  0), screen.window_height())
p2       = Paddle("blue", (-(screen.window_width() / 2) + 20,  0), screen.window_height())
p1_score = Score(( 50, (screen.window_height() / 2) - 50))
p2_score = Score((-50, (screen.window_height() / 2) - 50))
ball     = Ball()

screen.listen()
screen.onkey(p1.move_up  , "Up"  )
screen.onkey(p1.move_down, "Down")
screen.onkey(p2.move_up  , "w"   )
screen.onkey(p2.move_down, "s"   )

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()

    if (abs(ball.ycor()) + 10) >= (screen.window_height() / 2):
        ball.bounce_topbottom()
    
    if (ball.xcor() + 20 >= p1.xcor() - 10) and (ball.ycor() <= p1.ycor() + 50) and (ball.ycor() >= p1.ycor() - 50):
        ball.bounce_right()

    if (ball.xcor() - 20 <= p2.xcor() + 10) and (ball.ycor() <= p2.ycor() + 50) and (ball.ycor() >= p2.ycor() - 50):
        ball.bounce_left()

    if (ball.xcor() > (p1.xcor() - 10)):
        p2_score.score += 1
        ball.reset()
        ball.increase_speed()

    if (ball.xcor() < (p2.xcor() + 10)):
        p1_score.score += 1
        ball.reset()

    p1_score.update_score()
    p2_score.update_score()

screen.exitonclick()
