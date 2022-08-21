import math
a = [1, 2, 3, 4, 5, 6, 8, 20, 50, 70]
target = 50

def elementSearch(list, target):
  for item in list:
    if(item == target):
      return(True)
  return(False)

print(elementSearch(a, target))