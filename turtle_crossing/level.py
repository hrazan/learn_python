from turtle import Turtle


class Level(Turtle):
    def __init__(self, positon):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(positon)
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', False, align="left", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=('Arial', 50, 'bold'))
