from turtle import Turtle


class Score(Turtle):
    def __init__(self, positon):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(positon)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f'{self.score}', False, align="center", font=('Arial', 30, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=('Arial', 50, 'bold'))
