year = int(input("Enter a year to check: "))

if(year % 4 == 0 and year % 100 != 0):
  print("Its a leap year")
elif(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
  print("Its a leap year")
else:
  print("Not a leap year")