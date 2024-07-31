from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color("green")
        self.goto(0, 0)
        self.speed = 0.05
        self.direction = int(random.random() * 360)

    def reset(self):
        self.goto(0, 0)
        self.direction = int(random.random() * 360)

    def increase_speed(self):
        self.speed += 0.01

    def move(self):
        self.setheading(self.direction)
        self.forward(self.speed)

    def bounce_topbottom(self):
        self.direction = 360 - self.direction

    def bounce_right(self):
        if self.direction <= 90:
            self.direction = 180 - self.direction
        elif self.direction <= 180:
            pass
        elif self.direction <= 270:
            pass
        elif self.direction <= 360:
            self.direction = 540 - self.direction

    def bounce_left(self):
        if self.direction <= 90:
            pass
        elif self.direction <= 180:
            self.direction = 180 - self.direction
        elif self.direction <= 270:
            self.direction = 540 - self.direction
        elif self.direction <= 360:
            pass
