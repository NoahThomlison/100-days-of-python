from turtle import Turtle, Screen
import random

class SnakeGame():
  def __init__(self) -> None:
      pass

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")

snake = []
for xPos in range (0, 3):
  snakeBody = Turtle("square")
  snakeBody.color("white")
  snakeBody.penup()
  snakeBody.goto(xPos, 0)
  # snake.append(snakeBody)

print(snake)
gameOn = True

# while gameOn:
#   snake.forward(1)

# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()