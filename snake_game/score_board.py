from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, height - 20)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', False, align="center", font=('Arial', 12, 'normal'))        

