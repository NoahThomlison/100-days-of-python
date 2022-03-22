from re import I
from threading import currentThread
from turtle import Turtle, Screen
import random
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# def turn_left():
#   snakeSegments[0].left(90)

# def turn_right():
#   snakeSegments[0].right(90)

def createFood():
  xPos = random.randint(-300, 300)
  yPos = random.randint(-300, 300)
  xPos=int(round(xPos/20)*20)
  yPos=int(round(yPos/20)*20)

  food = Turtle("square")
  food.color("red")
  food.penup()
  food.goto(xPos, yPos)
  return(food)

gameOn = True
foodPresent = False
snake = Snake()

print(snake)
while gameOn:
  screen.onkey(key="a", fun=snake.turn_left)
  screen.onkey(key="d", fun=snake.turn_right)
  screen.update()
  time.sleep(.25)

  # if not foodPresent:
  #   food = createFood()
  #   foodPresent = True

  # print(snakeSegments[0].pos())
  # print(food.pos())

  # if(snakeSegments[0].pos() == food.pos()):
  #   food.reset()
  #   createSnakeSegments(1)
  #   del food
  #   foodPresent = False

  for index in range(len(snake.snakeSegments)-1, 0, -1):
    currentHead = snake.snakeSegments[index-1].pos()
    snake.snakeSegments[index].goto(currentHead)
  snake.snakeSegments[0].forward(20)



gameOn = True

screen.exitonclick()