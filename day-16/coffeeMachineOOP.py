from pickle import TRUE
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def runMachine():
  coffeeMachine = CoffeeMaker()
  moneyMachine = MoneyMachine()
  coffeeMenu = Menu()
  running = True

  while running == True:
    drinkOrder = input(f"What would you like to order? ({coffeeMenu.get_items()}) ")
    if(drinkOrder == "off"):
      running = False
    elif(drinkOrder == "report"):
      coffeeMachine.report()
      moneyMachine.report()
    else:
      drink = coffeeMenu.find_drink(drinkOrder)
      if(coffeeMachine.is_resource_sufficient(drink)):
        print(f"Your total is {drink.cost}")
        moneyPaid = moneyMachine.make_payment(drink.cost)
        if(moneyPaid):
          coffeeMachine.make_coffee(drink)

runMachine()