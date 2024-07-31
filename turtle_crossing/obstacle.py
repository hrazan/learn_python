from turtle import Turtle
import random


class Obstacle(Turtle):
    def __init__(self, random_direction, window_width, window_height):
        super().__init__()        
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color((random.random(), random.random(), random.random()))
        self.speed("fastest")
        self.__max_height = window_height / 2
        self.__max_width = window_width / 2
        self.__speed = random.random() * 0.1
        if random_direction:
            self.setheading(180 * random.randint(0, 1))
        else:
            self.setheading(180)

        if self.heading() >= 180:
            self.goto( self.__max_width + 40, random.randint(50, self. __max_height - 50))
        else:
            self.goto(-self.__max_width - 40, random.randint(50, self. __max_height - 50))

    def move(self):
        self.forward(self.__speed)

    def is_over(self):
        _is_over = False
        if self.heading() >= 180:
            if (self.xcor() + 30) < -self.__max_width:
                _is_over = True
        else:
            if (self.xcor() - 30) > self.__max_width:
                _is_over = True
        return _is_over