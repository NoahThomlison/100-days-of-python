from turtle import Turtle
import random

class Food():
  def __init__(self):
      self.isPresent = False
      self.location = []
      # self.clear_food()
      self.createFood()

  def createFood(self):
    if(self.isPresent):
      self.clear_food()
    xPos = random.randint(-300, 300)
    yPos = random.randint(-300, 300)
    xPos = int(round(xPos/20)*20)
    yPos = int(round(yPos/20)*20)

    food = Turtle("square")
    food.color("red")
    food.penup()
    food.goto(xPos, yPos)
    self.position = [xPos, yPos]
    return(food)

  def clear_food(self):
    Food.reset()