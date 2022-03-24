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