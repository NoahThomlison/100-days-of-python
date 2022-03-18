#####Turtle Intro######

from turtle import Turtle
from turtle import Screen
import random
import turtle
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.width(5)
tim.speed(5)

######## Challenge 2 - Buncha Shapes ############
def shape ():
  sides = 3
  while sides < 15:
    red = (random.randint(0, 255))
    blue = (random.randint(0, 255))
    green = (random.randint(0, 255))
    tim.color(red, blue, green) 	
    angle = 360/sides
    for _ in range (sides):
      tim.forward(50)
      tim.left(angle)
    sides += 1

shape()

tim.width(15)
tim.speed(10)
# screen.clear()

######## Challenge 3 - Random Walker ############
def walker():
  tim.clear()
  for x in range (0, 1000):
    direction = random.randint(0, 3)
    red = (random.randint(0, 255))
    blue = (random.randint(0, 255))
    green = (random.randint(0, 255))
    tim.color(red, blue, green) 	
    if(direction == 0):
      tim.forward(20)
    if(direction == 1):
      tim.left(90)
      tim.forward(20)
    if(direction == 2):
      tim.right(90)
      tim.forward(20)

walker()