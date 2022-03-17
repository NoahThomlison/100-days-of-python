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
}

def checkResources(order):
  haveIngredient = True
  for ingredient in MENU[order]["ingredients"]:
    print(MENU[order]["ingredients"][ingredient])
    print(resources[ingredient])
    if((MENU[order]["ingredients"][ingredient]) > (resources[ingredient])):
      print(f"You do not have enough {ingredient}. Please refill the machine")
      haveIngredient = False
  return(haveIngredient)


def takePayment():
  print("nothing")

def updateResources(drinkOrder):
  print("nothing")

def interface (MENU, resources):
  drinkOrder = input("What would you like to order? (espresso/latte/cappuccino) ")
  checkResources(drinkOrder)
  takePayment()
  updateResources(drinkOrder)

interface(MENU, resources)