from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Let's play the Snake Game")
screen.tracer(0)

s = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(s.up, 'Up')
screen.onkey(s.down, 'Down')
screen.onkey(s.right, 'Right')
screen.onkey(s.left, 'Left')

hit_the_wall = False
while not hit_the_wall:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(food) < 15:
        score.track_score()
        s.extend()
        food.move_food()

    if s.head.xcor() > 285:
        score.game_over()
        hit_the_wall = True
    elif s.head.xcor() < -285:
        score.game_over()
        hit_the_wall = True
    elif s.head.ycor() > 285:
        score.game_over()
        hit_the_wall = True
    elif s.head.ycor() < -285:
        score.game_over()
        hit_the_wall = True

    for snake in s.snake_segments[1:]:
        if s.head.distance(snake) < 10:
            hit_the_wall = True
            score.game_over()


screen.exitonclick()
