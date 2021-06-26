from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
distance = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle('square')
        new_snake.color('pink')
        new_snake.width(20)
        new_snake.penup()
        new_snake.goto(position)
        self.snake_segments.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for snake in range(len(self.snake_segments) - 1, 0, -1):
            new_xcor = self.snake_segments[snake - 1].xcor()
            new_ycor = self.snake_segments[snake - 1].ycor()
            self.snake_segments[snake].goto(new_xcor, new_ycor)
        self.head.forward(distance)

    def down(self):
        if self.head.heading() != 90: #when it's facing UP, it shouldn't be allowed to turn south.
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180: #when it's facing right, it shouldn't be allowed to turn left.
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0: #when it's facing left, it shouldn't be allowed to turn right.
            self.head.seth(180)

    def up(self):
        if self.head.heading() != 270: #when it's facing down, it shouldn't be allowed to turn up.
            self.head.seth(90)
