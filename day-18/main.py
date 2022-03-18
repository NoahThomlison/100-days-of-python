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

dots = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def homePosition(sizeOfPainting):
    tim.penup()
    tim.goto(-sizeOfPainting/2, -sizeOfPainting/2)

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


def goToStart(spacing):
    tim.left(90)
    tim.forward(spacing)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)



def printDots(spacing, sizeOfArray):
    rowIndex = 0
    for row in range (0, sizeOfArray):
        print(row)
        for column in range (0, sizeOfArray):
            tim.color(dots[random.randint(0, len(dots)-1)])
            tim.stamp()

            #if end condition, do not move forward
            if(column == sizeOfArray-1):
                break
            tim.forward(spacing)

        #if end condition, do not move forward
        if(row == sizeOfArray-1):
            break

        elif(row % 2 == 0):
            tim.left(90)
            tim.forward(spacing)
            tim.left(90)

        elif(row % 2 != 0):
            tim.right(90)
            tim.forward(spacing)
            tim.right(90)
        
    Screen().exitonclick()

tim.speed(10)
size = 500
array = 10
spacing = size/(array+1)
print(spacing)
homePosition(size)
drawBorder(size)
goToStart(spacing)
printDots(spacing, array)
