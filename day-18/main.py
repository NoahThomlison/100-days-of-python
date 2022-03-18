###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, circle
from turtle import Screen
import random
import turtle
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("circle")
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

dots = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def homePosition(sizeOfPainting):
    tim.penup()
    tim.left(180)
    tim.forward(sizeOfPainting/2)
    tim.left(90)
    tim.forward(sizeOfPainting/2)
    tim.left(90)

def drawBorder(sizeOfPainting):
    tim.pendown()
    tim.forward(sizeOfPainting)
    tim.left(90)
    tim.forward(sizeOfPainting)
    tim.left(90)
    tim.forward(sizeOfPainting)
    tim.left(90)
    tim.forward(sizeOfPainting)
    tim.penup()


def goToStart(offset):
    tim.left(180)
    tim.forward(offset)
    tim.right(90)
    tim.forward(offset)


def printDots(sizeOfPainting, sizeOfArray, offset):
    rowIndex = 0
    for row in range (0, sizeOfArray-1):
        for column in range (0, sizeOfArray-1):
            print(row, column)
            tim.stamp()
            randomDot = random.randint(0, len(dots)-1)

        if(row % 2 == 0):
            tim.stamp()
            tim.left(90)
            tim.forward(sizeOfPainting/sizeOfArray+2)
            tim.left(90)
        elif(row % 3 ==0 ):
            tim.stamp()
            tim.right(90)
            tim.forward(sizeOfPainting/sizeOfArray+2)
            tim.right(90)
        else:
            tim.color(dots[randomDot])
            tim.forward(sizeOfPainting/sizeOfArray+2)
            rowIndex += 1
    Screen().exitonclick()

tim.speed(10)
offset = 20
size = 300
array = 6
homePosition(size)
drawBorder(size)
goToStart(offset)
printDots(size, array, offset)
