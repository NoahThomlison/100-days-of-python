from functools import total_ordering


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "coins" : 0,
}

def checkResources(order):
  haveIngredient = True
  for ingredient in MENU[order]["ingredients"]:
    # print(MENU[order]["ingredients"][ingredient])
    # print(resources[ingredient])
    if((MENU[order]["ingredients"][ingredient]) > (resources[ingredient])):
      print(f"You do not have enough {ingredient}. Please refill the machine")
      haveIngredient = False
  return(haveIngredient)


def takePayment(order):
  print(f"Your order of {order} costs {MENU[order]['cost']}")
  quarters = int(input("How many quarters? "))
  dimes = int(input("How many dimes? "))
  nickles = int(input("How many nickles? "))
  pennies = int(input("How many pennies? "))
  totalPayment = quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
  
  if totalPayment < MENU[order]['cost']:
    print("You have not put in enough money. Please start over. Refunding deposited money")
    return(False)
  else:
    change = MENU[order]['cost'] - totalPayment
    print(f"Your change is {change}")
    resources["coins"] = MENU[order]['cost']

  print(resources["coins"])

def updateResources(drinkOrder):
  print("nothing")

def interface (MENU, resources):
  drinkOrder = input("What would you like to order? (espresso/latte/cappuccino) ")
  if checkResources(drinkOrder):
    takePayment(drinkOrder)

  updateResources(drinkOrder)

interface(MENU, resources)