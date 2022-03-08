print("Welcome to the tip calculator.")
totalBill = int(input("What was the total bill? "))
percantage = int(input("What percentage tip would you like to give? "))
numberOfPeople =  int(input("How many people  to split the bill? "))
individualCost = (totalBill * percantage/100 + totalBill) / numberOfPeople
print(f"Each person should pay {round(individualCost,2)}")