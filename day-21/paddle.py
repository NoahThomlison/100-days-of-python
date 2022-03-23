from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, side):
    super().__init__()
    self.speed("fastest")
    self.shape("square")
    self.penup()
    self.left(90)
    self.shapesize(stretch_len=5, stretch_wid=1)
    if side == "right":
      self.goto((350,0))
    if side == "left":
      self.goto((-350,0))
    self.color("white")

  def go_up(self):
    self.forward(40)

  def go_down(self):
    self.backward(40)

  # def checkImpact(self, ball):
  #   self

  #   screen.setup(width=800, height=600)
