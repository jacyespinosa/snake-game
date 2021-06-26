from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed('fastest')
        self.move_food()

    def move_food(self):
        random_xcor = random.randint(-280, 281)
        random_ycor = random.randint(-280, 281)
        self.goto(random_xcor, random_ycor)
