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
while gameOn:
  screen.onkey(key="a", fun=snake.turn_left)
  screen.onkey(key="d", fun=snake.turn_right)
  screen.update()
  time.sleep(.25)

  #Detect collision with food.
  if snake.head.distance(food) < 15:
      food.refresh()
      snake.eatFood()

  #Detect collision with wall.
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      game_is_on = False
      
  #Detect collision with tail.
  for segment in snake.snakeSegments:
      print(segment)
      print(snake.head.distance(segment))

      if segment == snake.head:
          pass
      elif snake.head.distance(segment) < 10:
          gameOn = False

  snake.move()


gameOn = True

screen.exitonclick()