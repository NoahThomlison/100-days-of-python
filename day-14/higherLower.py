logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


from math import fabs
from data import *
import random

def getIndex ():
  index = random.randint(0, len(data)-1)
  return index

def higherOrLower (firstIndex, secondIndex):
  if(int(data[firstIndex]["follower_count"])>int(data[secondIndex]["follower_count"])):
    return("a")
  else:
    return("b")

def game ():
  correctStreak = 0
  continueGame = True
  
  while continueGame:
    firstComparisionIndex = getIndex()
    secondComparisionIndex = getIndex()
    if(secondComparisionIndex == firstComparisionIndex):
      secondComparisionIndex = random.randint(0, len(data)-1)

    print("\nWho has more instagram followers?")
    print(f'A:{data[firstComparisionIndex]["name"]}:{data[firstComparisionIndex]["description"]}')
    print(vs)
    print(f'B:{data[secondComparisionIndex]["name"]}:{data[secondComparisionIndex]["description"]}')
    guess = input()
    guess = guess.lower()
    aOrB = higherOrLower(firstComparisionIndex, secondComparisionIndex)
    if((aOrB == "a" and guess == "a") or (aOrB == "b" and guess == "b")):
      print("You are right! ")
      print(f'A:{data[firstComparisionIndex]["name"]} has {data[firstComparisionIndex]["follower_count"]}')
      print(f'A:{data[secondComparisionIndex]["name"]} has{data[secondComparisionIndex]["follower_count"]}')
      correctStreak += 1
      print(f"Your current streak is {correctStreak}")
    else:
      print("You got it wrong")
      print(f'A:{data[firstComparisionIndex]["name"]} has {data[firstComparisionIndex]["follower_count"]}')
      print(f'A:{data[secondComparisionIndex]["name"]} has{data[secondComparisionIndex]["follower_count"]}')
      print(f"Your streak was {correctStreak}")
      continueGame = False

game()