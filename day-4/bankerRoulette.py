import random

name_string = input("Give me a list of names seperated by a comma. ")
splitNames = (name_string.split(", "))

print(f"{splitNames[random.randint(0, len(splitNames)-1)]} will pay the bill")

