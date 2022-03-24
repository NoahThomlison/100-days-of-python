from mimetypes import init
from turtle import Turtle

class Player(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.shape("turtle")
      self.speed("fastest")
      self.penup()
      self.left(90)
      self.goto(0, -280)
      self.speed("normal")
      self.color("black")

  def move_forward(self):
    self.forward(20)

  def move_back(self):
    self.back(20)

  def move_left(self):
    self.left(90)
    self.forward(20)
    self.right(90)

  def move_right(self):
    self.right(90)
    self.forward(20)
    self.left(90)

  def check_at_finish_line(self):
    if self.ycor() >= 280:
      return(True)