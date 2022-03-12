logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def doMath (number, secondNumber, operation):
  if operation == "+":
    answer = number + secondNumber
  elif operation == "-":
    answer = number - secondNumber
  elif operation == "*":
    answer = number * secondNumber
  elif operation == "/":
    answer = number / secondNumber
  return answer

print(logo)
moreMath = True
more = "n"
while moreMath == True:
  if more == "n":
    number = int(input("What is your first number: "))
    operation = input("What operation (+ - * / ): ")
    secondNumber = int(input("What is your second number: "))
  if more == "y":
    print(f"{answer} is your first number")
    number = answer
    operation = input("What operation (+ - * / ): ")
    secondNumber = int(input("What is your second number: "))

  answer = doMath(number, secondNumber, operation)

  print(f"{number} {operation} {secondNumber} = {answer}")
  more = input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation. ')
  more = more.lower()
  if more != "y" and more != "n":
    moreMath = False