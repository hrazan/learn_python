from turtle import Turtle


class Hero(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.ystart = (-screen_height / 2) + 30
        self.reset_position()
        
    def reset_position(self):
        self.goto(0, self.ystart)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())