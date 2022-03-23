from turtle import Turtle, xcor
import random

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("red")
    self.penup()
    starting_direction = random.randint(0, 360)
    print(starting_direction)
    self.left(30)
    self.x_move = 1
    self.y_move = 1

  def move_forward(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def checkImpactWithWalls(self):
    if(self.ycor() >= 300 or self.ycor() <= -300):
      self.y_move *= -1

  def checkImpactWithPaddle(self, paddle):
    paddlePosition = paddle.ycor()
    paddleTop = paddlePosition + 50
    paddleBottom = paddlePosition - 50
    paddleX = paddle.xcor()
    if (paddleX > 0):
      paddleEdge = paddleX - 10
    else:
      paddleEdge = paddleX + 10
    if(self.ycor() <= paddleTop and self.ycor() >= paddleBottom and self.xcor() == paddleEdge):
      self.x_move *= -1

  def checkIfMissed(self):
    print(self.xcor())
    if(self.xcor() >= 400):
      return("L")
    elif(self.xcor() <= -400):
      return("R")

  def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
