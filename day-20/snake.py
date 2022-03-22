from turtle import Turtle

class Snake():
  def __init__(self) -> None:
    self.positions = [(0,0), (-20, 0), (-40, 0)]
    self.snakeSegments = []
    self.createSegment(3)
    self.head = self.snakeSegments[0]

  def createSegment(self, numberOfSegments):
    for xPos in range (0, numberOfSegments):
      snakeBody = Turtle("square")
      snakeBody.color("white")
      snakeBody.penup()
      snakeBody.goto(self.positions[xPos])
      self.snakeSegments.append(snakeBody)

  def eatFood(self):
    snakeBody = Turtle("square")
    snakeBody.color("white")
    snakeBody.penup()
    position = self.positions[len(self.positions)-1]
    snakeBody.goto(position)
    self.positions.append(position)
    self.snakeSegments.append(snakeBody)

  def turn_left(self):
    self.snakeSegments[0].left(90)

  def turn_right(self):
    self.snakeSegments[0].right(90)

  def move(self):
    for index in range(len(self.snakeSegments)-1, 0, -1):
      currentHead = self.positions[index-1]
      self.snakeSegments[index].goto(currentHead)
      self.positions[index] = currentHead
    self.snakeSegments[0].forward(20)
    self.positions[0] = self.snakeSegments[0].pos()

  def getLocations(self):
    return(self.positions)