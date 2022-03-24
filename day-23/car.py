from mimetypes import init
from turtle import Turtle
import random
import time

colors = ["red", "blue", "orange", "green", "purple"]

class Car(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.shape("turtle")
      self.speed("fastest")
      self.shape("square")
      self.shapesize(stretch_len=2, stretch_wid=1)
      self.penup()
      self.left(180)
      self.speed("normal")
      self.color(colors[(random.randint(0, (len(colors) - 1)))])
      self.startingLocationY = random.randint(-200, 200)
      self.startingLocationX = -1 * random.randint(-1000, -300)
      self.goto(self.startingLocationX, self.startingLocationY)

  def move_forward(self):
    self.forward(20)
  
  def is_off_screen(self):
    if(self.xcor() > 500):
      del self
      return(False)