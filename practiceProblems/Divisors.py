number = int(input("Give me a number "))
i = number
divisors = []
while i > 0:
  if(number % i == 0):
    divisors.append(i)
  i = i - 1

print(divisors)