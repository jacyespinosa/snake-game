from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.setposition(x=0, y=280)
        self.pendown()
        self.hideturtle()
        self.add_point = 0
        self.write_score()

    def write_score(self):
        self.write("Score: {}".format(self.add_point), align="center", font=("Times New Roman", 20, "normal"))

    def track_score(self):
        self.add_point += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.penup()
        self.setposition(x=0, y=0)
        self.pendown()
        self.hideturtle()
        self.write("GAME OVER!!!", align="center", font=("Times New Roman", 50, "normal"))
        self.penup()
        self.setposition(x=0, y=-30)
        self.pendown()
        self.hideturtle()
        self.write("Final Score: {}".format(self.add_point), align="center", font=("Times New Roman", 20, "normal"))