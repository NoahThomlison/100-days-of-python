from re import I
from threading import currentThread
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

gameOn = True
foodPresent = False
snake = Snake()
food = Food()
array = []
print(snake)
while gameOn:
  screen.onkey(key="a", fun=snake.turn_left)
  screen.onkey(key="d", fun=snake.turn_right)
  screen.update()
  time.sleep(.25)
  snake.move()

  if(snake.positions[0] == food.position):
    food.clear_food()
    food.createFood()

gameOn = True

screen.exitonclick()