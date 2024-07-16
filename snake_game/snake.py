from turtle import Turtle


class Snake:
    def __init__(self):
        self.speed = 1.0
        self.__start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.__snake_bodies = []
        for position in self.__start_positions:
            _snake_body = Turtle(shape="square")
            _snake_body.color("white")
            _snake_body.penup()
            _snake_body.goto(position)
            self.__snake_bodies.append(_snake_body)

    def move(self):
        for i in range(len(self.__snake_bodies) - 1, 0, -1):
            self.__snake_bodies[i].goto((self.__snake_bodies[i - 1].pos()[0], self.__snake_bodies[i - 1].pos()[1]))
            # print(str(i) + " : " + str(self.__snake_bodies[i-1].pos()))

        self.__snake_bodies[0].forward(20)

    def move_left(self):
        self.__snake_bodies[0].left(90)

    def move_right(self):
        self.__snake_bodies[0].right(90)

