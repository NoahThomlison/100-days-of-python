from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Frogger")
screen.tracer(0)

frogger = Player()
game_on = True
numOfCars = 1
cars = []


for x in range(0, numOfCars):
  car = Car()
  cars.append(car)
print(cars)

x = 0
while game_on:
  screen.onkey(key="Up", fun=frogger.move_forward)

  for car in cars:
    car.move_forward()
    if(car.check_impact(frogger)):
      game_on = False
    if(car.is_off_screen()):
      cars.remove(car)
      car = Car()
      cars.append(car)
    screen.update()
  print(x)

print(cars)
screen.listen()
screen.exitonclick()
