from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.speed = 1.0
        self.__start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.__snake_bodies = []
        self.make_body()
        self.head = self.__snake_bodies[0]
        self.__is_increase_body = False

    def make_body(self):
        for position in self.__start_positions:
            _snake_body = Turtle(shape="square")
            _snake_body.color("white")
            _snake_body.penup()
            _snake_body.goto(position)
            self.__snake_bodies.append(_snake_body)

    def move(self):
        if self.__is_increase_body:
            _snake_body = Turtle(shape="square")
            _snake_body.color("white")
            _snake_body.penup()
            _snake_body.goto(self.__snake_bodies[len(self.__snake_bodies) - 1].pos())
            self.__snake_bodies.append(_snake_body)
            for i in range(len(self.__snake_bodies) - 2, 0, -1):
                self.__snake_bodies[i].goto(self.__snake_bodies[i - 1].pos())
            self.__is_increase_body = False
            # print(len(self.__snake_bodies))
        else:
            for i in range(len(self.__snake_bodies) - 1, 0, -1):
                self.__snake_bodies[i].goto(self.__snake_bodies[i - 1].pos())
                # print(str(i) + " : " + str(self.__snake_bodies[i-1].pos()))

        self.__snake_bodies[0].forward(20)
        # print(self.__snake_bodies[0].heading())

    def move_left(self):
        if self.__snake_bodies[0].heading() != LEFT and self.__snake_bodies[0].heading() != RIGHT:
            self.__snake_bodies[0].setheading(LEFT)

    def move_right(self):
        if self.__snake_bodies[0].heading() != LEFT and self.__snake_bodies[0].heading() != RIGHT:
            self.__snake_bodies[0].setheading(RIGHT)

    def move_up(self):
        if self.__snake_bodies[0].heading() != DOWN and self.__snake_bodies[0].heading() != UP:
            self.__snake_bodies[0].setheading(UP)

    def move_down(self):
        if self.__snake_bodies[0].heading() != DOWN and self.__snake_bodies[0].heading() != UP:
            self.__snake_bodies[0].setheading(DOWN)

    def increase_body(self):
        self.__is_increase_body = True

    def body_position(self):
        _body_positon = []
        print(len(self.__snake_bodies))
        for i in range(1, len(self.__snake_bodies), 1):
            _body_positon.append(self.__snake_bodies[i].pos())
        return _body_positon
