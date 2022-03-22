from turtle import Turtle

class Snake():
  def __init__(self) -> None:
      self.positions = [(0,0), (-20, 0), (-40, 0)]
      self.snakeSegments = []
      self.createSegment(3)

  def createSegment(self, numberOfSegments):
    for xPos in range (0, numberOfSegments):
      snakeBody = Turtle("square")
      snakeBody.color("white")
      snakeBody.penup()
      snakeBody.goto(self.positions[xPos])
      self.snakeSegments.append(snakeBody)

  def turn_left(self):
    self.snakeSegments[0].left(90)

  def turn_right(self):
    self.snakeSegments[0].right(90)