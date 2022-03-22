from re import I
from threading import currentThread
from turtle import Turtle, Screen
import random
import time

class SnakeGame():
  def __init__(self) -> None:
      pass

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

def turn_left():
  snakeSegments[0].left(90)

def turn_right():
  snakeSegments[0].right(90)

snakePosition = [(0,0), (-20, 0), (-40, 0)]
snakeSegments = []

for xPos in range (0, 3):
  snakeBody = Turtle("square")
  snakeBody.color("white")
  snakeBody.penup()
  snakeBody.goto(snakePosition[xPos])
  snakeSegments.append(snakeBody)

gameOn = True


while gameOn:
  screen.onkey(key="a", fun=turn_left)
  screen.onkey(key="d", fun=turn_right)
  screen.update()
  time.sleep(.5)
  print(len(snakeSegments))
  for index in range(len(snakeSegments)-1, -1, -1):
    currentHead = snakeSegments[index-1].pos()
    print(currentHead)
    print(index)
    if(index > 0):
      snakeSegments[index].goto(currentHead)
    else:
      snakeSegments[index].forward(20)

gameOn = True

screen.exitonclick()