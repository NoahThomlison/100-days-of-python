import math
a = [1, 2, 3, 4, 5, 6, 8, 20, 50, 70]
target = 3

def elementSearch(list, target):
  low = 0
  high = len(list) - 1 
  mid = (low + high)/2
  while low <= high:
    mid = low + (high - low)//2
    if list[mid] == target:
      return mid
    elif list[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
    return -1

print(elementSearch(a, target))