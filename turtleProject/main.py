from turtle import Turtle, Screen
import heroes as h
import random as rand

# turtle1 = Turtle()
screen1 = Screen()
screen1.colormode(255)
color = [(253, 253, 252), (250, 240, 246), (242, 249, 247), (236, 242, 250), (236, 209, 96), (233, 165, 72), (230, 158, 5), (208, 133, 170), (194, 5, 45), (21, 113, 198), (116, 170, 216), (206, 72, 125), (228, 168, 194), (166, 180, 171), (170, 49, 103), (210, 67, 7), (9, 165, 227), (244, 205, 2), (102, 103, 204), (184, 180, 224), (47, 28, 161), (231, 76, 44), (235, 170, 160), (146, 218, 186), (203, 14, 3), (86, 195, 29), (4, 104, 85), (138, 212, 229), (39, 127, 93), (99, 3, 25), (17, 14, 116), (3, 102, 110), (254, 7, 4), (254, 6, 30), (84, 121, 0)]

""" dashline
def dash(turtle_, length_):
    drawn_length = 0
    while drawn_length < length_:
        pendown_length = 0
        while pendown_length < 10:
            if drawn_length > length_:
                break
            turtle_.pendown()
            turtle_.forward(1)
            pendown_length += 1
            drawn_length += 1
        penup_length = 0
        while penup_length < 10:
            if drawn_length > length_:
                break
            turtle_.penup()
            turtle_.forward(1)
            penup_length += 1
            drawn_length += 1


def draw_shape_right(turtle_, side_length, shape_sides):
    turtle_.pendown()
    angle = 360.0 / shape_sides
    for i in range(shape_sides):
        turtle_.right(angle)
        turtle1.pencolor((rand.random(), rand.random(), rand.random()))
        turtle_.forward(side_length)


def draw_shape_left(turtle_, side_length, shape_sides):
    turtle_.pendown()
    angle = 360.0 / shape_sides
    for i in range(shape_sides):
        turtle_.left(angle)
        turtle1.pencolor((rand.random(), rand.random(), rand.random()))
        turtle_.forward(side_length)


screen1.screensize(canvwidth=300, canvheight=300)
turtle1.shape("turtle")
# turtle1.hideturtle()
turtle1.color("red")
"""

""" shape
for i in range(3, 20):
    draw_shape_right(turtle1, 50, i)
    draw_shape_left(turtle1, 50, i)
screen1.exitonclick()
#"""

""" random walk
step = 0
turtle1.pensize(5)
turtle1.speed(0)
turtle1.hideturtle()
while step < 1000:
    turtle1.pencolor((rand.random(), rand.random(), rand.random()))
    turtle1.right(rand.randint(0, 3) * 90)
    turtle1.forward(30)
#"""

""" spirograph
spiral_number = 100
spirograph_angle = 360 / spiral_number
turtle1.speed(0)
turtle1.hideturtle()
for i in range(spiral_number):
    turtle1.pencolor((rand.random(), rand.random(), rand.random()))
    turtle1.penup()
    turtle1.right(spirograph_angle)
    turtle1.forward(3)
    turtle1.pendown()
    turtle1.circle(100)
#"""

""" art
turtle1.hideturtle()
turtle1.penup()
turtle1.back(100)
turtle1.right(90)
turtle1.forward(100)
turtle1.left(90)

for i in range(10):
    for j in range(10):
        turtle1.dot(10, rand.choice(color))
        turtle1.forward(20)
    turtle1.back(200)
    turtle1.left(90)
    turtle1.forward(20)
    turtle1.right(90)
"""

"""
def move_forward():
    turtle1.forward(1)


def move_back():
    turtle1.back(1)


def rotate_right():
    turtle1.right(1)


def rotate_left():
    turtle1.left(1)


def turn_right():
    new_heading = turtle1.heading() + 1
    turtle1.setheading(new_heading)
    # turtle1.right(1)


def turn_left():
    turtle1.left(1)


def reset_drawing():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()


screen1.listen()
screen1.onkeypress(move_forward, "w")
screen1.onkeypress(move_back, "s")
screen1.onkeypress(rotate_left, "a")
screen1.onkeypress(rotate_right, "d")
screen1.onkeypress(turn_right, "q")
screen1.onkeypress(turn_right, "e")
screen1.onkey(reset_drawing, "c")
"""


def move_forward(turtle_):
    turtle_.forward(1)


def move_back(turtle_):
    turtle_.back(1)


def rotate_right(turtle_):
    turtle_.right(1)


def rotate_left(turtle_):
    turtle_.left(1)


def turn_right(turtle_):
    turtle_.right(1)


def turn_left(turtle_):
    turtle_.left(1)


def reset_drawing(turtle_):
    turtle_.clear()
    turtle_.penup()
    turtle_.home()
    turtle_.pendown()


is_not_finish = False
screen1.setup(width=700, height=500)
bet = int(screen1.textinput(title="win the bet", prompt="which turtle win? 1/2/3/4/5 ?")) + 1

turtles = []
for i in range(5):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(rand.choice(color))
    turtles[i].penup()
    turtles[i].goto(-330, 150 - (75 * i))

if bet:
    is_not_finish = True

final_position = []
winner = 99
finished_turtle = 0
print(f"{len(turtles)} turtles will race!")
while is_not_finish:
    for i in range(len(turtles)):
        turtles[i].forward(rand.randint(0, 10))
        if turtles[i].pos()[0] >= 300:
            if i not in final_position:
                final_position.append(i)
                finished_turtle += 1
                if finished_turtle == 1:
                    winner = i
                elif finished_turtle >= len(turtles):
                    is_not_finish = False

if bet == winner:
    print("you WIN!")
else:
    print("you LOSE!")
print("Final position:")
print(f"the winner is turtle {winner}!")
for i in range(len(final_position)):
    print(f"position {i+1}: turtle {final_position[i]+1}")


screen1.listen()
screen1.exitonclick()
