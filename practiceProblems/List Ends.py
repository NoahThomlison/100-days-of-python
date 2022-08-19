a = [5, 10, 15, 20, 25]

def ends (a):
  ends = []
  for index, element in enumerate(a):
    if(index == 0 or index == len(a)-1):
      ends.append(element)
  return(ends)

print(ends(a))