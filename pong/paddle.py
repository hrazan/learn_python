from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, color, position, height):
        super().__init__()        
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(color)
        self.speed("fastest")
        self.goto(position)
        self.__max_height = height / 2
        self.__step = 30

    def move_up(self):
        # if (self.ycor() + self.__step) <= self.__max_height:
        #     self.goto(self.pos()[0], self.pos()[1] + self.__step)
        
        self.goto(self.pos()[0], min(self.pos()[1] + self.__step, self.__max_height))

    def move_down(self):
        if (self.ycor() - self.__step) >= -self.__max_height:
            self.goto(self.pos()[0], self.pos()[1] - self.__step)
        